#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <stdio.h>

int size_of_file(std::string filel) {
    FILE *file = NULL;
    file = fopen(filel.c_str(), "rb");
    fseek(file, 0, SEEK_END);
    int size = ftell(file);
    fclose(file);
    return size;
}

int count_lines(std::string file) {
    int count_s;
    std::string line;
    count_s = 0;
    std::ifstream in(file);
    if (in.is_open()) {
        while (getline(in, line)) {
            count_s++;
        }
        return count_s;
    }
}

int count_words(std::string file) {
    char c2;
    std::string line;
    int count_sl;
    count_sl = 0;
    std::ifstream in(file);
    if (in.is_open()) {
        while (getline(in, line)) {
            for (int i = 0; i < line.length(); ++i) {
                c2 = line.c_str()[i];

                if (c2 == ' ' || c2 == '\n' || c2 == '\t') {
                    count_sl++;
                }
            }
        }
        in.close();
        return count_sl;
    }
}

int main(int argc, char *argv[]) {
    bool flag_l;
    bool flag_w;
    bool flag_c;
    std::string chek;
    std::string filepoint;
    for (int i = 1; i < argc; i++) { // looking for a file
        if (count_lines(argv[i]) >= 0 and (size_of_file(argv[i]) >= 0)) {
            filepoint = argv[i];
        }
    }

    std::cout << "Labwork1!\n";
    for (int i = 1; i < argc; i++) {
        chek = argv[i];
        if ((chek == "-l") or (chek == "--lines")) {
            std::cout << argv[i] << std::endl;
            flag_l = true;
            continue;
        } // Cheking arguments
        else if ((chek == "-c") or (chek == "--bytes")) {
            std::cout << argv[i] << std::endl;
            flag_c = true;
            continue;
        }
        else if ((chek == "-w") or (chek == "--words")) {
            std::cout << argv[i] << std::endl;
            flag_w = true;
            continue;
        }
        else{
            if (chek == "-lwc"){
                flag_l = true;
                flag_c = true;
                flag_w = true;
                continue;
            }
            else if (chek == "-lcw"){
                flag_l = true;
                flag_c = true;
                flag_w = true;
                continue;
            }
            else if (chek == "-cwl"){
                flag_l = true;
                flag_c = true;
                flag_w = true;
                continue;
            }
            else if (chek == "-clw"){
                flag_l = true;
                flag_c = true;
                flag_w = true;
                continue;
            }
            else if (chek == "-wlc"){
                flag_l = true;
                flag_c = true;
                flag_w = true;
                continue;
            }
            else if (chek == "-wcl"){
                flag_l = true;
                flag_c = true;
                flag_w = true;
                continue;
            }
            else{
                if (chek == "-cl" or chek == "-lc"){
                    flag_l = true;
                    flag_c = true;
                    continue;
                }
                else if(chek == "-lw" or chek == "-wl"){
                    flag_l = true;
                    flag_w = true;
                    continue;
                }
                else if(chek == "-cl" or chek == "-lc"){
                    flag_l = true;
                    flag_c = true;
                    continue;
                }
            }
        }
    }

    if (argc == 2) { //if no arguments printing all
        std::cout << "Lines count:" << count_lines(argv[1]) << std::endl << "Word count:" << count_words(argv[1])
                  << std::endl
                  << "File size:" << size_of_file(argv[1]) << std::endl;
    }

    else if (argc > 2) { // have argument
        if (flag_l) {
            std::cout << "Lines count:" << count_lines(filepoint) << std::endl;
        }
        if (flag_c) {
            std::cout << "File size:" << size_of_file(filepoint) << std::endl;
        }
        if (flag_w) {
            std::cout << "Word count:" << count_words(filepoint) << std::endl;
        }
        std::cout << "End of program" << std::endl;
        return 0;
    }
}   