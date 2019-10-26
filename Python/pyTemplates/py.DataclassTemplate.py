from dataclasses import dataclass, field
import typing

@dataclass
class Employee(object):
    id: int
    name: str
    title: str

    
Employee(id=1,name='Bill',title='Head Guy')

