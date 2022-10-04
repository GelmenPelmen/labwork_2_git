#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <sstream>

int size_of_file(std::string filename)
{
    FILE* file = NULL;
    file = fopen(filename.c_str(), "rb");
    fseek(file, 0, SEEK_END);
    int size = ftell(file);
    fclose(file);
    return size;
}

/*int ochistka(std::string filename) {
    std::string s1;
    std::string s2;
    std::string s3;
    std::string b = filename;
    std::ostringstream ss;
    ss << s1 << "" << s2;
    std::string s = ss.str();
    if (s == "-l" and s == "--" and s == "-c" and s == "-w") {
        for(int i = )
    }
    ss << s << "" << s3;
    std::string b = ss.str();
    }
*/

int main(int argc, char* argv[])
{
    for (int i = 1; i < argc; i++) {
        std::cout << argv[i] << std::endl;
    }
    return 0;
}
    std::cout << "Labwork1!\n";
    std::string line;;
    std::string filename;
    std::string test;
    std::cin >> filename;
    std::string s1;
    std::string s2;
    std::string s3;
    s1 = filename[0];
    s2 = filename[1];
    s3 = filename[2];
    char c2;
    int count_s, count_sl;
    count_s = count_sl = 0;
    std::cout << argv[0] << argv[1] << argv[2] << std::endl;
    std::ostringstream ss;
    ss << s1 << "" << s2;
    std::string s = ss.str();
    ss << s << "" << s3;
    std::string b = ss.str();

    if (argc == 2) {

        std::ifstream in(filename);
        if (in.is_open()) {
            while (getline(in, line)) {
                count_s++;
                for (int i = 0; i < line.length(); ++i) {
                    c2 = line.c_str()[i];

                    if (c2 == ' ' || c2 == '\n' || c2 == '\t')
                    {
                        count_sl++;
                    }
                }
            }
            std::cout << "Lines count:" << count_s << std::endl << "Word count:" << count_sl << std::endl << "File size:" << size_of_file(filename) << std::endl;
            in.close();

        }
    }
    if (argc == 3) {
        if (s == "-l") {
            std::cout << test << "DA\n";
            std::cout << test;
        }
        std::ifstream in(filename);
        if (in.is_open()) {
            while (getline(in, line)) {
                count_s++;
            }
            std::cout << "Lines count:" << count_s << std::endl;
        }
        std::cout << "End of program" << std::endl;
        return 0;
    }
}
