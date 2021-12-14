#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
  string myText;
  int lastNum = 10000;
  int currNum;
  int increases;
  cout << "Hello World!\n";
  ifstream MyReadFile("input-1.txt");

  while (getline (MyReadFile, myText)) {
  // Output the text from the file
    currNum = std::stoi( myText );
    if(currNum > lastNum){
        increases++;
    }
    lastNum = currNum;
  }
  cout << increases;     
  return 0;
}