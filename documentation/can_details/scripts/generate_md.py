import yaml, os

SIZES = {   # Bit-Sizes
    'u8': 8,
    'u16': 16,
    'u32': 32,
    'u64': 32,
    'i8': 8,
    'i16': 16,
    'i32': 32,
    'i64': 32,
    'f32': 32,
    'f64': 32,
    'bool': 8,

    'u3': 3,
    'u4': 4,
    'u5': 5,
    'u8[3]': 24,
    'u8[4]': 32,
    'u8[6]': 48,
    'u8[7]': 56,
    'u8[8]': 64,

    'HwVersion': 32,
    'FwVersion': 32,
}


class Item():
    fmt = "    {:<4}{:<25}{:<10}{:<45}\n"
    fmt_ = "    " + " "*39 + "{:<45}\n" 

    def __init__(self, adr: int, content: dict):
        self.content = content
        self.adr = adr
        self.name = content['name']
        self.type = content['type']
        self.unit = content['unit']

    @classmethod
    def header(cls):
        h = cls.fmt.format('No', 'Datapoint', 'Type', 'Unit / Comment')
        h += '    ' + '-'*92 +'\n'
        return h

    def to_md(self):
        b_addr = self.adr // 8
        if self.adr % 8 == 0:
            no_str = f"{b_addr}"
        else:
            min = self.adr % 8
            no_str = f"{b_addr}.{min}"
        u_list = self.unit.split('\n')

        md = self.fmt.format(no_str, self.name, self.type, u_list[0])
        if len(u_list) > 1:
            for l in u_list[1:-1]:
                md += self.fmt_.format(l)
        return md

class Datapoint():
    fmt = "ID {} {}\n---\nName: {}  \nObject-ID Version: {}  \nType: {}  \nInterval: {}  \nLength: {} Bytes  \nDynamic Id: {}\n\n"
    def __init__(self, preferred_id, content: dict, generic = False):
        self.generic = generic
        self.content = content
        self.items = []
        self.id = content['id']
        self.name = content['name']
        self.object_id_ver = content['object_id_ver']
        self.type = content['type']
        self.comment = content['comment']
        self.interval = content['interval']
        self.preferred_id = preferred_id
        if type(self.interval) == int:
            self.interval = f"{self.interval} ms"
        adr = 0
        if content['data'] is not None:
            for dl in content['data']:
                item = Item(adr, dl)
                self.add_item(item)
                adr += SIZES[item.type]
        self.length = adr // 8
        if adr % 8 > 0:
            self.length += 1

    def add_item(self, line):
        self.items.append(line)
        
    def to_md(self):
        if self.preferred_id is None:
            preferred = '-'
        else:
            if self.generic:
                preferred = f'0x{self.id + 0x400 + self.preferred_id*16:03x}'
                dyn_id = f"Id(Heartbeat) + 0x{self.id:02x}"
            else:
                preferred = f'0x{self.id + self.preferred_id*16:03x}'
                dyn_id = f"Id(Heartbeat) - 0x400 + 0x{self.id:02x}"
            r = self.fmt.format(
            preferred,
            self.comment, 
            self.name,
            self.object_id_ver, 
            self.type, 
            self.interval, 
            self.length,
            dyn_id
        )
        r += Item.header()
        for item in self.items:
            r += item.to_md()
        r += '\n'
        return r

class DataObject():
    fmt = "    {:<45}{:<35}\n"

    def __init__(self, content: dict):
        # print(content)
        self.content = content
        self.name = content['name']
        self.name_ = content['name'].lower().replace(' ', '_')
        self.comment = content['comment']
        self.object_id = content['object_id']
        self.preferred_id = content['preferred_id']
        self.datapoints = []
        for dp in content['datapoints']:
            self.datapoints.append(Datapoint(self.preferred_id, dp))

    def add_generic_dps(self, content):
        for dp in content['datapoints']:
            self.datapoints.append(Datapoint(self.preferred_id, dp, generic=True))

    def to_md(self):
        id = self.preferred_id
        if id is None:
            generic_range = 'see specific profile'
            specific_range = 'not applicable'
        else:
            generic_range = f"0x{(0x400 + id*16):03x} - 0x{(0x40f + id*16):03x}"
            specific_range = f"0x{(id*16):03x} - 0x{(0xf + id*16):03x}"
        r = self.name + '\n===\n\n'
        r += self.fmt.format('Name', self.name_)
        r += self.fmt.format('Object Id', self.object_id)
        r += self.fmt.format('Preffered IDs for Specific Datapoints', specific_range)
        r += self.fmt.format('Preffered IDs for Generic Datapoints', generic_range)
        r += self.fmt.format('Comment', self.comment)
        r += '\n'
        for dp in self.datapoints:
            r += dp.to_md()
        return r

def generate(yaml_file, generics):
    print(f"processing '{yaml_file}'")
    with open(yaml_file, "r") as f:
        page = yaml.safe_load(f)

    do = DataObject(page)
    if yaml_file not in ('../yaml/arbitration.yaml', '../yaml/config.yaml'):
        do.add_generic_dps(generics)
    
    page_str = do.to_md()
    md_file = yaml_file.replace('../yaml/', '').replace('yaml', 'md')
    with open('../object_directory/' + md_file, 'w') as f:
        f.write(page_str)

with open("../yaml/generic.yaml", "r") as f:
    generics = yaml.safe_load(f)

for file in os.listdir('../yaml'):
    fname = '../yaml/' + file
    if os.path.isfile(fname) and file.find('.yaml') > 0 and file !='generic.yaml':
        generate(fname, generics)

