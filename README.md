# Privat24 ATM Finder 🏧

A utility for locating PrivatBank branches and ATMs with filtering by city and service type.

## 🔍 Features

- Find PrivatBank branches and ATMs
- Filter by city (supports Cyrillic)
- Identify service types (cash, terminals, etc.)
- Read data from local JSON files
- Command-line interface

## 📋 Requiremenets
1. Python3
2. Python3-pip
3. Internet connection
4. Docker (optional)

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Andrey-oss/Privat24-ATM-Finder.git
cd Privat24-ATM-Finder
```
2. Install dependencies:

```bash
pip3 install -r requirements.txt
```
🚀 Usage

```bash
python main.py
```

## 🐳 Docker
If you wish to run it by docker:

1. Start the service

```bash
sudo systemctl start docker
```

2. Build a container:

```bash
docker build -t Privat24-ATM-Finder .
```

3. Run the app:

```bash
docker run --rm -it mini_sherlock
```

## Future development
You can start develop this project by own:

* You can use *init_venv.sh* script. It will initialize virtualenv and install requirements from the file
* You can develop it inside the docker with mounting by typing:
```bash
docker run --rm -it -v $(pwd):/app mini_sherlock username
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/your-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin feature/your-feature)
5. Open a Pull Request

## 📜 License
MIT License. See LICENSE for details.