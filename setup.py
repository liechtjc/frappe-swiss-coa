from setuptools import setup, find_packages

setup(
    name="swiss_coa",
    version="0.0.1",
    description="Swiss SME Chart of Accounts for ERPNext (EN + FR)",
    author="Jean-Christophe Liechti",
    author_email="liechtjc@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
