## NameNinja : Github available usernames scanner
A Python script to check the availability of GitHub usernames. This tool generates usernames based on specific patterns and checks their availability using multi-threading for optimal performance.

## Setup

Follow these steps to set up the project and start using **NameNinja**:

1. **Clone the repository:**

   Clone the project repository to your local machine using the following command:

```bash
git clone https://github.com/Anbeh/NameNinja
```

2. **Navigate to the project directory:**
   
   After cloning, change to the project directory:
```bash
cd NameNinja
```

3. **Install dependencies:**

   Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

4. **Run the script:**
Once the dependencies are installed, run the script:

```bash
python NameNinja.py <username_length> <num_threads> [-l] [-d]
```
- `<username_length>`: Specify the length of the usernames (e.g., 6).
- `<num_threads>`: Specify the number of threads to use for checking the usernames (e.g., 10).
- `-l`: If you want to generate usernames with letters only, include this flag.
- -`d`: If you want to generate usernames with digits only, include this flag.

If both -l and -d are provided, the script will generate usernames with letters and digits.

The output will look something like this:

```bash
⠀⠀⠀⠀⠀⣀⠠⠄⠒⠒⠒⠠⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢆⠀⠀⠀⠀⠀⠀
⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀
⠀⠀⢸⠀⢀⢴⡂⠉⠁⠀⠈⠉⠐⠢⡀⠀⡇⠀⠀⠀⠀⠀
⠀⠀⢸⠀⡇⠀⢻⣿⠂⠀⠐⣿⣿⠁⠈⠄⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠣⡱⣀⠈⠉⠀⠀⠀⠈⠁⣀⠜⡘⠀⠀⡠⡞⣍⡂
⠀⠀⠀⠀⠀⢢⡥⠐⣒⣒⣒⡒⢬⡔⠊⢰⣶⡮⡱⡬⠚⠁
⠀⠀⠀⢀⠔⠉⠀⠀⠀⠀⠀⠀⠀⠈⠲⡊⣑⢵⠏⠀⠀⠀
⠀⠀⡠⠃⠀⢠⠀⠀⠀⠀⠀⠀⠀⣄⠀⠈⢇⠀⠀
⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉

Generated 456976 usernames.
Total usernames to check: 453201
Checking: 5950/453201 | Current: crtz
```

The script will generate a list of usernames and check their availability on GitHub. Results will be saved in the following files:
- `good.txt` for available usernames.
- `checked.txt` for taken usernames.

This script focuses on identifying available usernames but includes banned or restricted usernames in the results since they are technically not in use.

## Contributing

Feel free to fork the project and submit pull requests with improvements or bug fixes. Contributions are welcome!


## License
This project is open-source and available under the [MIT License.](https://choosealicense.com/licenses/mit/)

