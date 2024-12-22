from setuptools import find_packages,setup
from typing import List
hyp = "-e ."
def get_requirements(file_path:str)->List[str]:
    ''' this function will retuinr lst iof re 
    '''
    requirements = []
    with open(file_path) as file_obj:
      requirements=file_obj.readlines()
      requirements = [req.replace("\n","") for req in requirements]
      if hyp in requirements:
         requirements.remove(hyp)
    return requirements


setup(
     name = "up",
      
      version ="0.01",
      author = "sahith",
      author_email='sahithvamsi94@gmail.com',
      packages = find_packages(),
      install_requires = get_requirements("requirements.txt"),

)