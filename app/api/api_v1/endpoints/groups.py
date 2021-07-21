from fastapi import APIRouter, HTTPException
from app.core.settings import settings
from ldap3 import Server, Connection, ALL, SUBTREE

router = APIRouter(prefix="/groups", tags=["groups"])

@router.get('/{group}')
async def groups( group:str ):
    server = Server(settings.LDAP_URL)
    conn = Connection(server,user=settings.LDAP_UN,password=settings.LDAP_PW)
    conn.bind()
    conn.search('ou=Groups,dc=dms,dc=local', f'(cn={group})', attributes=['member'])
    result = conn.entries
    if len(result) > 1:
        return HTTPException(status_code=500, detail="Too many groups")
    if len(result) == 0:
        return HTTPException(status_code=404, detail="Group Not Found")

    group = result[0].entry_dn
    users = result[0].member.values

    results = []
    for u in users:
        conn.search( f"{u}",f'(&(objectClass=person)(objectClass=user)(employeeID=*)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))', attributes = ['sAMAccountName','employeeID'] )
        if len(conn.entries) <= 0:
            continue
        username = conn.entries[0].sAMAccountName.value
        badge = conn.entries[0].employeeID.value
        results.append(badge)
    return results
    