import os
from typing import  List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, validator, SecretStr
from pydantic.types import FilePath
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    LDAP_URL: str = "ldap://openldap"
    LDAP_UN: str = "cn=admin,dc=dms,dc=local"
    LDAP_PW: str = "Adm1n!"
    #LDAP_URL: str = "ldap://ad.dallasmakerspace.org"
    #LDAP_UN: str = "cn=jwtest_svc,ou=service,ou=users,ou=admin,dc=dms,dc=local"
    #LDAP_PW: str = ""
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True


settings = Settings( basedir + "/.env")
