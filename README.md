# Encryption-Via-Vigenere-Cipher
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
--> 

<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h3 align="center">Viginere Encryption ReadMe</h3>

  <p align="center">
    ID# 202101453

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started </a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project 


In the PDF file you'll find the pages for each of the following
</br>
Introduction page-3
</br>
Instructions for running the program page-4
</br>
Unit tests page-5
</br>
Discerption of work page-6
</br>
Source Code page-7
</br>
References page-7
</br>
Figure1 page-3
</br>
Figure2 page-5
</br>
FIgure3 page-5
</br>







### 


<!-- USAGE EXAMPLES -->
## Instructions for Running the Program

Firstly, the user will be prompted to choose between encrypt, decrypt, or if he/she wants to exit the program by reading the prompted questions the user will find what to type in between single quotations, depending on the user’s answers and inputs the program will execute the right code for the job. In the case the user chooses to encrypt, they will be asked if they want to encrypt their own self typed text which can be chosen by typing ‘text’ or choose an existing file that contains text by typing ‘file’, then (in the case of choosing the ‘file’ command) the user will be prompted to type the name of the file with respect of spelling and typing the file type following the name. After that the user will be prompted to choose a method of using the key to encrypt whether to generate a random key that will generate a key that consist of not less than 3 and not more than 9 characters so it’ll be a reasonable number of characters not too large and not so little that encryption of the text would be easy to decrypt  which can be accessed by typing ‘1’, self-type in the key which can be accessed by typing ‘2’, or to import a key from an existing file or created previously by the user which can be accessed by typing ‘3’. And of course, all this with respect of spelling and typing the file type following the name, furthermore whichever method the user will choose the key will be saved in a file named as the user wants and in addition to the ciphered text in a separate file. As for how the key works, a key generator function was developed to ensure that the key has the same length as the text, and if the key’s length already matches that of the text’s the function will just use the key without editing it. The encryption works using the encrypt function which is defined in the program. It adds the placement of each character’s value in the ascii code list from the text to each character’s value in the ascii code list in the key and with the help of the math equation given and range given.  
(If the user misspells words and forget to type the file type the program will prompt the user to retype the phrases, he/she wrote wrong).
Next if the user chooses to decrypt the program will ask the user to input the name of the file they want to decrypt, then the program opens the file and reads its content, next the user will be prompted to type in the file that has the key that was used to encrypt the phrase in the previously chosen file, furthermore the program opens the key file and then reads its content. Finally, the program takes both files decrypts them using the decrypt function and lists the text in a new file. The decrypt function is the opposite of the encrypt function instead of adding each character from the text to each character in the key it subtracts them so it can trace back the placement in the range give in the ascii code list and with the help of the math equation given.

[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
