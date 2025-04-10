def decor(function):
    def inner(name):
        if name == 'Ayush':
            print(name, 'Likes Briyani')

        else: 
            return function(name)
        return inner
@decor
def process(name):
    print(name, 'likes pulao')

process('Ankita')
process('Akash')
process('ayush')
process('Punith')