from sys import argv
from src.common import new_file_path
from src.lib import encrypt


def add_decrypt_func(data):
    header = "class GalaxyProtector():\n def __decode__(self:object,_execute:str)->exec:return(None,self._cum(_execute))[0]\n def __init__(self:object,_bytes:str=True,_AES256:int=0,*_ras:float,**_system:int)->exec:\n  self._orgasm,_bytes,_system[_AES256],self._encrypt,self._eval,self._cum=exit()if _bytes else'abcdefghijklmnopqrstuvwxyz0123456789',lambda _bytes:exit()if self._orgasm[15]+self._orgasm[17]+self._orgasm[8]+self._orgasm[13]+self._orgasm[19] in open(__file__, errors=self._orgasm[8]+self._orgasm[6]+self._orgasm[13]+self._orgasm[14]+self._orgasm[17]+self._orgasm[4]).read() or self._orgasm[8]+self._orgasm[13]+self._orgasm[15]+self._orgasm[20]+self._orgasm[19] in open(__file__, errors=self._orgasm[8]+self._orgasm[6]+self._orgasm[13]+self._orgasm[14]+self._orgasm[17]+self._orgasm[4]).read()else\"\".join(_bytes if _bytes not in self._orgasm else self._orgasm[self._orgasm.index(_bytes)+1 if self._orgasm.index(_bytes)+1<len(self._orgasm)else 0]for _bytes in \"\".join(chr(ord(t)-810353)if ord(t)!=950else\"\\n\"for t in self._encrypt(_bytes))),eval,lambda _delete:\"\".join(__import__(self._orgasm[1]+self._orgasm[8]+self._orgasm[13]+self._orgasm[0]+self._orgasm[18]+self._orgasm[2]+self._orgasm[8]+self._orgasm[8]).unhexlify(str(_bits)).decode()for _bits in str(_delete).split('/')),lambda _bytes:str(_system[_AES256](f\"{self._orgasm[4]+self._orgasm[-13]+self._orgasm[4]+self._orgasm[2]}(''.join(%s),{self._orgasm[6]+self._orgasm[11]+self._orgasm[14]+self._orgasm[1]+self._orgasm[0]+self._orgasm[11]+self._orgasm[18]}())\"%list(_bytes))).encode(self._orgasm[20]+self._orgasm[19]+self._orgasm[5]+self._orgasm[34])if _system[_AES256]==eval else exit(),lambda _AES256:self._eval(_bytes(_AES256))\n  return self.__decode__(_system[(self._orgasm[-1]+'_')[-1]+self._orgasm[18]+self._orgasm[15]+self._orgasm[0]+self._orgasm[17]+self._orgasm[10]+self._orgasm[11]+self._orgasm[4]])\nGalaxyProtector(_bytes=False,_AES256=False,_sparkle='''" + data + "''') "

    return header


def main():
    print("START")
    if len(argv) == 2 and argv[1]:
        code = open(argv[1], "r").read()
        result = add_decrypt_func(encrypt(code))
        with open(new_file_path('e', argv[1]), "w") as f:
            f.write(result)
    else:
        print("Arguments:\n"
              "\tpath\tthe path to the file\n"
              "Output:\n"
              "\tCreat a file with the basename of the given path with e or d at the start separate by a '_'")


if __name__ == '__main__':
    main()
