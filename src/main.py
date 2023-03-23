from lexer import Lexer
from parser import Parser

def main():
    # example code to parse
    code = '''
func process() {
    var x = 123;
    var y = "hello, world!";
    set_gain(x + 456);
    if (x > 100) {
        return y;
    } else {
        for i = 0, 10 {
            delay(i);
        }
        break;
    }
}
'''


    tokens = list(Lexer(code))


    print("Tokens:")
    print(tokens[:60])


    ast = Parser(code)

    

    print("\nGenerated AST:")
    print(ast)

if __name__ == "__main__":
    main()

