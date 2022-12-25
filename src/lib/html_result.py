from dataclasses import dataclass

@dataclass
class HTMLResult:
    status: int
    title: str
    body: str