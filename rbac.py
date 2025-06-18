class Permission:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Permission('{self.name}')"

    def __eq__(self, other):
        return isinstance(other, Permission) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

class Role:
    def __init__(self, name: str):
        self.name = name
        self.permissions = set() 

    def add_permission(self, permission: Permission):
        self.permissions.add(permission)

    def has_permission(self, permission: Permission) -> bool:
        return permission in self.permissions

    def __repr__(self):
        return f"Role('{self.name}')"

class User:
    def __init__(self, username: str):
        self.username = username
        self.roles = set() # Usamos um set para evitar papéis duplicados

    def assign_role(self, role: Role):
        self.roles.add(role)

    def has_permission(self, permission: Permission) -> bool:
        for role in self.roles:
            if role.has_permission(permission):
                return True
        return False

    def __repr__(self):
        return f"User('{self.username}')"

# Def. do Cenário: Sistema de Gestão de Conteúdo 

# Criando as permissões disponíveis no sistema  Permissions
perm_create_article = Permission("create_article")
perm_edit_own_article = Permission("edit_own_article")
perm_edit_any_article = Permission("edit_any_article")
perm_publish_article = Permission("publish_article")
perm_delete_article = Permission("delete_article")
perm_manage_users = Permission("manage_users")

# Criando os papéis (Roles)
role_colaborador = Role("Colaborador")
role_editor = Role("Editor")
role_administrador = Role("Administrador")

# Atribuindo permissões aos papéis (Permission-Role Assignment)
role_colaborador.add_permission(perm_create_article)
role_colaborador.add_permission(perm_edit_own_article)

role_editor.add_permission(perm_create_article)
role_editor.add_permission(perm_edit_any_article)
role_editor.add_permission(perm_publish_article)
role_editor.add_permission(perm_delete_article)

# O Administrador herda todas as permissões do Editor e tem mais algumas
for perm in role_editor.permissions:
    role_administrador.add_permission(perm)
role_administrador.add_permission(perm_manage_users)


# Demonst. prática

# Criando usuários
user_ana = User("Ana")
user_bruno = User("Bruno")
user_carla = User("Carla")

# Atribuindo papéis aos usuários (User-Role Assignment)
user_ana.assign_role(role_colaborador)
user_bruno.assign_role(role_editor)
user_carla.assign_role(role_administrador)

# Verificando as permissões de cada usuário
print("--- Verificando Permissões ---\n")

# Cenário 1: Ana (Colaboradora) tenta criar um artigo.
print(f"Usuária: {user_ana.username} (Papel: {list(user_ana.roles)[0].name})")
print(f"Pode criar artigos? -> {user_ana.has_permission(perm_create_article)}") # Esperado: True
print(f"Pode publicar artigos? -> {user_ana.has_permission(perm_publish_article)}") # Esperado: False
print(f"Pode gerenciar usuários? -> {user_ana.has_permission(perm_manage_users)}") # Esperado: False
print("-" * 25)

# Cenário 2: Bruno (Editor) tenta publicar um artigo e gerenciar usuários.
print(f"Usuário: {user_bruno.username} (Papel: {list(user_bruno.roles)[0].name})")
print(f"Pode criar artigos? -> {user_bruno.has_permission(perm_create_article)}") # Esperado: True
print(f"Pode publicar artigos? -> {user_bruno.has_permission(perm_publish_article)}") # Esperado: True
print(f"Pode gerenciar usuários? -> {user_bruno.has_permission(perm_manage_users)}") # Esperado: False
print("-" * 25)

# Cenário 3: Carla (Administradora) tenta tudo.
print(f"Usuária: {user_carla.username} (Papel: {list(user_carla.roles)[0].name})")
print(f"Pode publicar artigos? -> {user_carla.has_permission(perm_publish_article)}") # Esperado: True
print(f"Pode gerenciar usuários? -> {user_carla.has_permission(perm_manage_users)}") # Esperado: True
print("-" * 25)

# Cenário 4: E se um usuário tiver múltiplos papéis?
user_david = User("David")
user_david.assign_role(role_colaborador)
user_david.assign_role(role_editor) # David é colaborador e também editor

print(f"Usuário: {user_david.username} (Papéis: {[r.name for r in user_david.roles]})")
# A permissão vem do papel de Editor
print(f"Pode publicar artigos? -> {user_david.has_permission(perm_publish_article)}") # Esperado: True
print("-" * 25)