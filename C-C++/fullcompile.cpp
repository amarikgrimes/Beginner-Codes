#include <iostream>
#include <fstream>
#include <cctype>
#include <cstring>

using namespace std;

// function prototypes
void addChar();
void getChar();
void getNonBlank();
int lex();
int lookup(char ch);
void expr();   // <expr> function
void term();   // <term> function
void factor(); // <factor> function

// global variables
int charClass;
char lexeme[100];
char nextChar;
int lexLen;
int token;
int nextToken;
ifstream in_fp;

#define LETTER 0
#define DIGIT 1
#define UNKNOWN 99
#define INT_LIT 10
#define IDENT 11
#define ASSIGN_OP 20
#define ADD_OP 21
#define SUB_OP 22
#define MULT_OP 23
#define DIV_OP 24
#define LEFT_PAREN 25
#define RIGHT_PAREN 26
#define EQUALS_OP 27 // new token for '=='

// function to lookup operators and parentheses
int lookup(char ch) {
    switch (ch) {
        case '(':
            addChar();
            nextToken = LEFT_PAREN;
            break;
        case ')':
            addChar();
            nextToken = RIGHT_PAREN;
            break;
        case '+':
            addChar();
            nextToken = ADD_OP;
            break;
        case '-':
            addChar();
            nextToken = SUB_OP;
            break;
        case '*':
            addChar();
            nextToken = MULT_OP;
            break;
        case '/':
            addChar();
            nextToken = DIV_OP;
            break;
        case '=':
            addChar();
            getChar(); // look ahead for ==
            if (nextChar == '=') {
                addChar();
                nextToken = EQUALS_OP; // token for '=='
            } else {
                nextToken = ASSIGN_OP; // token for '='
            }
            break;
        default:
            addChar();
            nextToken = EOF;
            break;
    }
    return nextToken;
}

// function to add character to lexeme
void addChar() {
    if (lexLen <= 98) {
        lexeme[lexLen++] = nextChar;
        lexeme[lexLen] = 0;
    } else {
        cout << "error - lexeme is too long\n";
    }
}

// function to get the next character of input and classify it
void getChar() {
    if (in_fp.get(nextChar)) {
        if (isalpha(nextChar))
            charClass = LETTER;
        else if (isdigit(nextChar))
            charClass = DIGIT;
        else
            charClass = UNKNOWN;
    } else {
        charClass = EOF;
    }
}

// function to remove whitespace
void getNonBlank() {
    while (isspace(nextChar)) {
        getChar();
    }
}

// lexical analyzer
int lex() {
    lexLen = 0;
    getNonBlank(); // remove any leading whitespace
    switch (charClass) {
        case LETTER:
            addChar();
            getChar();
            while (charClass == LETTER || charClass == DIGIT) {
                addChar();
                getChar();
            }
            nextToken = IDENT;
            break;
        case DIGIT:
            addChar();
            getChar();
            while (charClass == DIGIT) {
                addChar();
                getChar();
            }
            nextToken = INT_LIT;
            break;
        case UNKNOWN:
            lookup(nextChar);
            getChar();
            break;
        case EOF:
            nextToken = EOF;
            strcpy(lexeme, "EOF");
            break;
    }
    cout << "next token is: " << nextToken << ", next lexeme is " << lexeme << "\n";
    return nextToken;
}

// <factor> ::= IDENT | INT_LIT | '(' <expr> ')'
void factor() {
    if (nextToken == IDENT || nextToken == INT_LIT) {
        // match identifier or integer literal
        lex();
    } else if (nextToken == LEFT_PAREN) {
        // handle '(' <expr> ')'
        lex();
        expr(); // evaluate the expression within parentheses
        if (nextToken == RIGHT_PAREN) {
            lex(); // consume the closing ')'
        } else {
            cout << "error: missing closing parenthesis\n";
        }
    } else {
        cout << "error: invalid factor\n";
    }
}

// <term> ::= <factor> { (*|/) <factor> }
void term() {
    factor(); // parse the first factor
    while (nextToken == MULT_OP || nextToken == DIV_OP) {
        lex(); // consume '*' or '/'
        factor(); // parse the next factor
    }
}

// <expr> ::= <term> { (+|-) <term> }
void expr() {
    term(); // parse the first term
    while (nextToken == ADD_OP || nextToken == SUB_OP) {
        lex(); // consume '+' or '-'
        term(); // parse the next term
    }
}

int main() {
    // open the input file
    in_fp.open("front.in");
    if (!in_fp) {
        cerr << "error - cannot open front.in\n";
        return 1;
    } else {
        getChar();  // initialize reading from input
        lex();      // call the lexer to get the first token
        expr();     // start parsing with <expr>
        if (nextToken != EOF) {
            cout << "error: end of file expected\n";
        } else {
            cout << "parsing completed successfully.\n";
        }
    }
    return 0;
}
