import builtins

def greet(name=None):
    if name is None:
        name = input("What's your name?")
    print('Hello, ' + name)

def test_greet(capsys):
    greet('World')
    captured = capsys.readouterr()
    assert captured.out == 'Hello, World\n'

def test_greet_input(capsys, monkeypatch):
    def fake_input(question):
        print(question)
        return "Petr"

    monkeypatch.setattr(builtins, 'input', fake_input)
    greet()
    captured = capsys.readouterr()
    assert captured.out == "What's your name?\nHello, Petr\n"
