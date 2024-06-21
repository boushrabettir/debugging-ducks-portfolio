from dataclasses import dataclass

@dataclass
class Project:
    name: str
    desc: str

class User:
    def __init__(self) -> None:  
        self.hobbies = [
            {"name": "Football", "img_code": "fb"},
            {"name": "Video Games", "img_code": "vg"},
            {"name": "Watching Aurora", "img_code": "au"}
        ]
        self.work_experience = ["SWE", "SWE Intern"]
        self.education = ["B.Sc."] 
        self.projects: Project = [
            Project(name='Block-Chain', desc='AI fraud detection.'),
            ]
            