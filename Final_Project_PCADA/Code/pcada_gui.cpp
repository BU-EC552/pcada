#include <iostream>
#include <fstream>
#include <SFML/Graphics.hpp>
#include <stdlib.h>
#include <string>
#include <vector>
using std::ifstream; 
using std::string;
using std::vector;
using std::cout;
using std::endl;

#define NUM_COMPANIES 5

int main() 
{
    // DECLARE ALL OF THE RECTANGULAR INPUT BOXES
	sf::RenderWindow window(sf::VideoMode(1000, 800), "PCADA");
	sf::RectangleShape Addgene(sf::Vector2f(125.f, 50.f));
	Addgene.setFillColor(sf::Color::Blue);
	Addgene.setPosition(40, 100);

	sf::RectangleShape DNASU(sf::Vector2f(125.f, 50.f));
	DNASU.setFillColor(sf::Color::White);
	DNASU.setPosition(40, 160);

	sf::RectangleShape iGEM(sf::Vector2f(125.f, 50.f));
	iGEM.setFillColor(sf::Color::White);
	iGEM.setPosition(40, 220);

	sf::RectangleShape input_box(sf::Vector2f(600.f, 50.f));
    input_box.setFillColor(sf::Color::White);
    input_box.setPosition(300, 100);

    sf::RectangleShape fafsa_filebox(sf::Vector2f(600.f, 50.f));
	fafsa_filebox.setFillColor(sf::Color::White);
	fafsa_filebox.setPosition(300, 200);

	sf::Font font;
	font.loadFromFile("/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf");

    // DECLARE THE TEXT BOXES
    sf::Text title;
    title.setFont(font);
    title.setString("PCADA");
    title.setFillColor(sf::Color::Red);
    title.setStyle(sf::Text::Bold);
    title.setPosition(40,40);

    sf::Text text_Addgene;
	text_Addgene.setFont(font);
	text_Addgene.setString("Addgene");
	text_Addgene.setFillColor(sf::Color::Black);
	text_Addgene.setStyle(sf::Text::Bold);
	text_Addgene.setPosition(40,100);

	sf::Text text_DNASU;
	text_DNASU.setFont(font);
	text_DNASU.setString("DNASU");
	text_DNASU.setFillColor(sf::Color::Black);
	text_DNASU.setStyle(sf::Text::Bold);
	text_DNASU.setPosition(40,160);

	sf::Text text_iGEM;
	text_iGEM.setFont(font);
	text_iGEM.setString("iGEM");
	text_iGEM.setFillColor(sf::Color::Black);
	text_iGEM.setStyle(sf::Text::Bold);
	text_iGEM.setPosition(40,220);

	string input_text;
	sf::Text text_input;
	text_input.setFont(font);
	text_input.setString("Enter the path to the FASTA file: ");
	text_input.setFillColor(sf::Color::Blue);
	text_input.setStyle(sf::Text::Bold);
	text_input.setPosition(300, 100);

    string file_path;
    sf::Text path_box;
    path_box.setFont(font);
	path_box.setString(file_path);
	path_box.setFillColor(sf::Color::Blue);
	path_box.setStyle(sf::Text::Bold);
	path_box.setPosition(300, 200);

    string selectedDB = "addgene";
    window.setFramerateLimit(30);

    // While the program is still running
    while (window.isOpen()) 
    {
        sf::Event event;
        while (window.pollEvent(event)) 
        {
            if (event.type == sf::Event::Closed)
                window.close();
            
            // If the user starts typing, update the file path to the target file
            else if (event.type == sf::Event::TextEntered) 
            {
                if (std::isprint(event.text.unicode))
                {
                    file_path += event.text.unicode;
                    path_box.setString(file_path);
                }
            }
            // If the user presses an arrow key, responsd to the direction by selecting the appropriate input database
            else if (event.type == sf::Event::KeyPressed) 
            {
      	        if (event.key.code == sf::Keyboard::Up) 
                {
                    if (Addgene.getFillColor() == sf::Color::Blue) 
                    {
                        Addgene.setFillColor(sf::Color::White);
                        DNASU.setFillColor(sf::Color::White);
                        iGEM.setFillColor(sf::Color::Blue);
                        selectedDB = "igem";
                    }
                    else if (iGEM.getFillColor() == sf::Color::Blue) 
                    {
                        Addgene.setFillColor(sf::Color::White);
                        DNASU.setFillColor(sf::Color::Blue);
                        iGEM.setFillColor(sf::Color::White);
                        selectedDB = "dnasu";
                    }
                    else if (DNASU.getFillColor() == sf::Color::Blue) 
                    {
                        Addgene.setFillColor(sf::Color::Blue);
                        DNASU.setFillColor(sf::Color::White);
                        iGEM.setFillColor(sf::Color::White);
                        selectedDB = "addgene";
                    }
                } 
                if (event.key.code == sf::Keyboard::Down) 
                {
                    if (Addgene.getFillColor() == sf::Color::Blue) 
                    {
                        Addgene.setFillColor(sf::Color::White);
                        DNASU.setFillColor(sf::Color::Blue);
                        iGEM.setFillColor(sf::Color::White);
                        selectedDB = "dnasu";
                    }
                    else if (iGEM.getFillColor() == sf::Color::Blue) 
                    {
                        Addgene.setFillColor(sf::Color::Blue);
                        DNASU.setFillColor(sf::Color::White);
                        iGEM.setFillColor(sf::Color::White);
                        selectedDB = "addgene";
                    }
                    else if (DNASU.getFillColor() == sf::Color::Blue) 
                    {
                        Addgene.setFillColor(sf::Color::White);
                        DNASU.setFillColor(sf::Color::White);
                        iGEM.setFillColor(sf::Color::Blue);
                        selectedDB = "igem";
                    }
                } 
                if (event.key.code == sf::Keyboard::BackSpace) 
                {
                    if (!file_path.empty()) 
                    {
                        file_path.pop_back();
                        path_box.setString(input_text);
                    }
                }
                // If the user presses enter, begin the main PCADA application
                if (event.key.code == sf::Keyboard::Return) 
                {
                    if (!file_path.empty()) 
                    {
                        ifstream (file_path, std::ifstream::in);
                        path_box.setString("GENERATING CONFIG FILES...");
                        window.draw(path_box);

                        // Run the configuration_manager.py script, generating the config files
                        system("python3 config_manager.py");

                        // For each config file, execute the example Repp command using the selected database, 
                        // user-input DNA sequence, and current config file
                        for (int i = 0; i < NUM_COMPANIES; i++)
                        {
                            string repp_string = "repp make seq -i " + file_path + " -o output" + std::to_string(i+1) + ".json" + " --" + selectedDB + " --settings " + "config" + std::to_string(i+1) + ".yaml -v";
                            system(repp_string.c_str());
                        }

                        // Once all of the Repp calls are complete, calculate the primerscore - for now, just print to terminal
                        for (int i = 0; i < NUM_COMPANIES; i++)
                        {
                            string score_string = "python3 primerscore.py output" + std::to_string(i+1) + ".json";
                            system(score_string.c_str());
                        }

                        // Generate visualizations of the Repp-compliant design for each of the input configuration files
                        for (int i = 0; i < NUM_COMPANIES; i++)
                        {
                            string vis_string = "python3 visualizer.py output" + std::to_string(i+1) + ".json";
                            system(vis_string.c_str());

                        }
                        // Update the text box letting the user know the program is complete
                        path_box.setString("BUILD COMPLETE, CHECK OUTPUT FILES");
                    }
                }
            }
        }
        // Draw all of the shapes!
        window.clear();
        window.draw(Addgene);
        window.draw(DNASU);
        window.draw(iGEM);

        window.draw(title);

        window.draw(text_Addgene);
        window.draw(text_DNASU);
        window.draw(text_iGEM);

        window.draw(input_box);
        window.draw(text_input);
        window.draw(fafsa_filebox);
        window.draw(path_box);
        window.display();
    }
    return 0;
}