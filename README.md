<div align="center">
    <h1 align="center">rangeKeyDict</h1>
    <p align="center">
    A dictionary that accepts ranges as keys
    <br />
    <a href="https://github.com/silvs110/rangeKeyDict/issues">Report Bug</a>
    ·
    <a href="https://github.com/silvs110/rangeKeyDict/issues">Request Feature</a>
    </p>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Apache License 2.0][license-shield]][license-url]

</div>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#disclaimer">Disclaimer</a></li>
  </ol>
</details>

## About The Project
A dictionary that accepts ranges as keys. The value can be acccessed by using a number in between the range keys. 

## Prerequisites
1. Python 3.8+

## Usage
````
range_dict = RangeKeyDict()
range_dict[(0, 10)] = 5
range_dict[(-5, -1)] = 1
range_dict[(11, 13)] = 0
print(range_dict) # {(0, 10): 5, (-5, 0): 1, (10, 13): 0}
print(range_dict[0]) # 5
print(range_dict[12]) # 0
print(range_dict[-5,-1]) # 1
range_dict[(0,10)] = 100
print(range_dict[0]) # 100
range_dict[-5,-1] = 35
print(range_dict[-3]) #35
````
See `sample.py` for more examples.
<!-- LICENSE -->
## License

Distributed under Apache License 2.0. See [`LICENSE`](https://github.com/silvs110/RangeKeyDict/blob/main/LICENSE) 
for more information.

[contributors-shield]: https://img.shields.io/github/contributors/silvs110/rangeKeyDict.svg?style=for-the-badge
[contributors-url]: https://github.com/silvs110/rangeKeyDict/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/silvs110/rangeKeyDict.svg?style=for-the-badge
[forks-url]: https://github.com/silvs110/rangeKeyDict/network/members
[stars-shield]: https://img.shields.io/github/stars/silvs110/rangeKeyDict.svg?style=for-the-badge
[stars-url]: https://github.com/silvs110/rangeKeyDict/stargazers
[issues-shield]: https://img.shields.io/github/issues/silvs110/rangeKeyDict.svg?style=for-the-badge
[issues-url]: https://github.com/silvs110/rangeKeyDict/issues
[license-shield]: https://img.shields.io/github/license/silvs110/rangeKeyDict.svg?style=for-the-badge
[license-url]: https://github.com/silvs110/rangeKeyDict/blob/master/LICENSE