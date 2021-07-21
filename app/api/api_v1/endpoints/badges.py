from typing import Any
from fastapi import APIRouter,  HTTPException
from app.core.settings import settings
from ldap3 import Server, Connection, ALL, SUBTREE

router = APIRouter(prefix="/badges", tags=["badges"])

@router.get('/{badge}')
async def groups( badge:str ):
    # TODO: Setup common query structure?
    server = Server(settings.LDAP_URL)
    conn = Connection(server,user=settings.LDAP_UN,password=settings.LDAP_PW)
    conn.bind()
    conn.search('ou=Members,dc=dms,dc=local', f'(employeeID={badge})', attributes=['memberOf'])
    member = conn.entries
    if len(member) > 1:
        return HTTPException(status_code=500, detail="Bad Badge Number")
    if len(member) == 0:
        return HTTPException(status_code=404, detail="Bad Badge number")

    result = []
    for g in member[0].memberOf.values:
        conn.search(g, '(objectClass=group)', attributes=['cn'])
        if len(conn.entries) <= 0:
            continue
        result.append({
            "name": conn.entries[0].cn.value,
            "dn": conn.entries[0].entry_dn
        })
    return result
    # results = []
    # for u in users:
    #     #conn.search( "ou=Members,dc=dms,dc=local",f'(sAMAccountName=user1)', attributes = ['sAMAccountName','employeeID'] )
    #     conn.search( f"{u}",f'(objectClass=person)', attributes = ['sAMAccountName','employeeID'] )
    #     if len(conn.entries) <= 0:
    #         continue
    #     username = conn.entries[0].sAMAccountName.value
    #     badge = conn.entries[0].employeeID.value
    #     results.append({"username":username, "badge":badge})
    # return results
    