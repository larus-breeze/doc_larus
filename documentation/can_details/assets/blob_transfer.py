# data transfer via CAN bus

TRANS_INIT = 0
TRANS_CRC = 1
TRANS_DATA = 2
TRANS_END = 3
ITER_STOP = 4

class Transfer():
    def __init__(self, blob: bytes):
        self.blob = blob
        self.blob_len = len(blob)
        self.blob_crc = self._crc
        self.blob = self.blob + bytes(7 - (self.blob_len % 7))

    def __iter__(self):
        self.dg_cnt = 0
        self.state = TRANS_INIT
        return self

    def __next__(self):
        if self.state == TRANS_INIT:
            dg = TRANS_INIT.to_bytes(1, 'little') + \
                 b'\x00\x00\x00' + \
                 self.blob_len.to_bytes(4, 'little')
            self.state = TRANS_CRC
            return dg
        elif self.state == TRANS_CRC:
            dg = TRANS_CRC.to_bytes(1, 'little') + \
                 b'\x00\x00\x00' + \
                 self.blob_crc()
            self.state = TRANS_DATA
            return dg
        elif self.state == TRANS_DATA:
                idx = self.dg_cnt * 7
                dg = (TRANS_DATA | ((self.dg_cnt & 0x3f) << 2)).to_bytes(1, 'little') + self.blob[idx:idx+7]
                self.dg_cnt += 1
                if self.dg_cnt == len(self.blob) / 7 - 1:
                    self.state = TRANS_END
                return dg
        elif self.state == TRANS_END:
            idx = self.dg_cnt * 7
            dg = (TRANS_END | ((self.dg_cnt & 0x3f) << 2)).to_bytes(1, 'little') + self.blob[idx:idx + 7]
            self.state = ITER_STOP
            return dg
        else:
            raise StopIteration

    def _crc(self) -> bytes:
        # calculate smt32_crc of self.blob
        crc=0xffffffff
        buf = bytearray()
        for b in self.blob:
            buf.insert(0, b)
            if len(buf) == 4:
                for val in buf:
                    crc ^= val << 24
                    for _ in range(8):
                        crc = crc << 1 if (crc & 0x80000000) == 0 else (crc << 1) ^ 0x104c11db7
                buf = bytearray()
        return crc.to_bytes(4, 'little')


data = b'This is a test to show that everything works'

t = Transfer(data)
dg_len = 0
for dg in t:
    dg_state = dg[0] & 0x03
    if dg_state == TRANS_INIT:
        dg_len = int.from_bytes(dg[4:], 'little')
        print(f"    can_id: 0x03, dg.upload_state: {dg[0] & 0x03}, dg.length: {dg_len}")
    elif dg_state == TRANS_CRC:
        print(f"    can_id: 0x03, dg.upload_state: {dg[0] & 0x03}, dg.crc: 0x{int.from_bytes(dg[4:], 'little'):04x}")
    elif dg_state == TRANS_DATA:
        print(f"    can_id: 0x03, dg.upload_state: {dg[0] & 0x03}, dg.block_count: {dg[0] >> 2}, data: {dg[1:]}")
    elif dg_state == TRANS_END:
        l = dg_len % 7 + 1
        print(f"    can_id: 0x03, dg.upload_state: {dg[0] & 0x03}, dg.block_count: {dg[0] >> 2}, last_data: {dg[1:]}")




