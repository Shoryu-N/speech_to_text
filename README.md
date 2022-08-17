### Environment
macOS Big Sur 11.5
Python 3.9.6

### Preparation

Install `requests` with pip.

Example command

- pip3 install requests


If pip is not installed, update to Python 3.4 or later.

### How to check if it works

Download the project locally and run ``python3 main.py`` in the root of the project.
Then enter the relative path of the .flac audio file under the project, followed by the word you want to search for, separated by a single space.
(We have placed a file named audio-sample.flac to check the operation.)
The position of the word will be displayed in the form of 0indexed to indicate a range. For example, if you search for the word "audio" and it is the first two letters, it will display (0, 2).
(If you have ever touched Python, you can imagine how to count in Python slices.)

- Example of how it works
````
$ python3 main.py
Enter the relative path of the audio_file
audio-sample.flac
Enter the words you want to search, separated by a single space.

Examples:
---------------「音声」の検索結果---------------
- 出現位置
(0, 2)
- 前後5文字も含めた文字列
音声認識の現状

- 出現位置
(31, 33)
- 前後5文字も含めた文字列
い最近では音声認識でもデ

---------------「現状」の検索結果---------------
- 出現位置
(5, 7)
- 前後5文字も含めた文字列
音声認識の現状について教

---------------「あああ」の検索結果---------------
````

If there are no hits in the search results, such as "あああ" in the above example, nothing will be displayed.

### Regarding Tests
 
- Based on the object-oriented principle, only public methods that can be referenced by other objects are tested.
- When using a tested module, we mock that module and check only if it is called.


### Reference Books

- Practical Object-Oriented Design in Ruby: (Author: Sandi Metz)
- Refactoring (2nd Edition): (Author:Martin Fowler)
