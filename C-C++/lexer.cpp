//amari grimes
//theory programming 
//in this program i am creating a lexer from the class textbook in c++ and testing it out with an input file example from that same textbook


#include <iostream>
#include <fstream>
#include <cctype>
#include <cstring>

using namespace std;

int charClass;
char lexeme[100];
char nextChar;
int lexLen;
int token;
int nextToken;
ifstream in_fp;

void addChar();
void getChar();
void getNonBlank();
int lex();
int lookup(char ch);

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
        cout << "Error - lexeme is too long\n";
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

// Function to remove whitespace
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
    cout << "Next token is: " << nextToken << ", Next lexeme is " << lexeme << "\n";
    return nextToken;
}

int main() {
    in_fp.open("front.in");
    if (!in_fp) {
        cerr << "ERROR - cannot open front.in\n";
        return 1;
    } else {
        getChar();
        do {
            lex();
        } while (nextToken != EOF);
    }
    return 0;
}

