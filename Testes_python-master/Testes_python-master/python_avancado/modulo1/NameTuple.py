from collections import namedtuple
Subscriber = namedtuple('Credenciais', ['login', 'senha'])
sub = Subscriber('michel@gmail.com', '123456')

print(sub)
print(sub.login)
print(sub.senha)
