import yaml, os

SIZES = {   # Bit-Sizes
    'u8': 8,
    'u16': 16,
    'u32': 32,
    'i8': 8,
    'i16': 16,
    'i32': 32,
    'f32': 32,
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
    fmt = "ID 0x{:02x} {}\n---\nName: {}  \nType: {}  \nInterval: {}  \nLength: {} Bytes\n\n"
    def __init__(self, content: dict):
        self.content = content
        self.items = []
        self.id = content['id']
        self.name = content['name']
        self.type = content['type']
        self.comment = content['comment']
        self.interval = content['interval']
        if type(self.interval) == int:
            self.interval = f"{self.interval} ms"
        adr = 0
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
        r = self.fmt.format(self.id, self.comment, self.name, self.type, self.interval, self.length)
        r += Item.header()
        for item in self.items:
            r += item.to_md()
        r += '\n'
        return r

class DataObject():
    fmt = "    {:<25}{:<45}\n"

    def __init__(self, content: dict):
        self.content = content
        self.name = content['name']
        self.name_ = content['name'].lower().replace(' ', '_')
        self.comment = content['comment']
        self.object_id = content['object_id']
        self.datapoints = []
        for dp in content['datapoints']:
            self.datapoints.append(Datapoint(dp))

    def to_md(self):
        r = self.name + '\n===\n\n'
        r += self.fmt.format('Name', self.name_)
        r += self.fmt.format('Object Id', self.object_id)
        r += self.fmt.format('Comment', self.comment)
        r += '\n'
        for dp in self.datapoints:
            r += dp.to_md()
        return r

def generate(yaml_file):
    print(f"processing '{yaml_file}'")
    with open(yaml_file, "r") as f:
        page = yaml.safe_load(f)

    do = DataObject(page)
    page_str = do.to_md()

    md_file = yaml_file.replace('yaml', 'md')
    with open('../object_directory/' + md_file, 'w') as f:
        f.write(page_str)

for file in os.listdir('.'):
    if os.path.isfile(file) and file.find('.yaml') > 0:
        generate(file)

