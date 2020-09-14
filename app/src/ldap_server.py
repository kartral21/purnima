from ldap3 import Server, Connection, ALL

LDAP_URL = 'ldap.forumsys.com'
USER = 'tesla'
PASSWORD = 'password'

from ldap3 import Server, Connection, ALL
class LDAP():
    def ldap_connection(self):
        total_entries = 0
        server = Server('ipa.demo1.freeipa.org', get_info=ALL)
        conn = Connection(server, 'uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org', 'Secret123', auto_bind=True)
        conn.search('dc=demo1,dc=freeipa,dc=org', '(objectclass=person)')
        search=conn.entries
        print("data",search)
        conn.add('ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'organizationalUnit')
        # Add a new user
        conn.add('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Beatrix', 'sn': 'Young', 'departmentNumber': 'DEV', 'telephoneNumber': 1111})
        detail=server.schema.object_classes['inetOrgPerson']
        conn.search('ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', '(cn=b.young)', attributes=['objectclass', 'sn', 'cn', 'givenname'])
        add=conn.entries[0]
        print(add)
        conn.modify_dn('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'cn=b.smith')
        conn.search('ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', '(cn=b.smith)', attributes=['objectclass', 'sn', 'cn', 'givenname'])
        modify=conn.entries[0]
        print(modify)
        total_entries += len(conn.response)
        for entry in conn.response:
            print(entry['dn'], entry['attributes'])
        # perform a Delete operation
        message_id = conn.delete('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')
        # perform the Abandon operation
        delete= conn.abandon(message_id)
if __name__ == "__main__":
    ldap = LDAP()
    ldap.ldap_connection()