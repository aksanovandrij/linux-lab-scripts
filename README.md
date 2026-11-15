# Linux Lab Scripts

Колекція Bash-скриптів для лабораторних робіт
з курсу "Системне програмування та адміністрування ОС".

## Вміст

- `count_files.sh` - скрипт для підрахунку файлів у /etc. Він входить у пакети rpm і deb і встановлюється як '/usr/bin/count_files'
- `count_files_ext.sh` - розширена версія: файли, директорії та посилання окремо. НЕ входить у пакети

- `packaging/rpm/` - spec-файл для збірки rpm (лаб 4) (+ кольорові повідомлення при встановленні та видаленні пакета)
- `packaging/deb/debian/` - файли для збірки deb (лаб 5)

- `.github/workflows/build-packages.yml` - GitHub Actions: збірка rpm і deb (лаб 6)
- `jenkins/`, `docker-compose.yml` - Jenkins master і agent у Docker (лаб 7)

- `Jenkinsfile` - pipeline: збірка пакетів, встановлення в контейнерах і запуск скрипта (лаб 8)

## Використання

```bash
./count_files.sh
./count_files_ext.sh
```

Встановлення пакета (готові пакети є в артефактах [GitHub Actions](https://github.com/aksanovandrij/linux-lab-scripts/actions/runs/43764954313#artifacts) та Jenkins):

```bash
sudo dpkg -i count-files_1.0-1_all.deb            # Debian / Ubuntu
sudo rpm -ivh count-files-1.0-1.fc45.noarch.rpm   # Fedora / RHEL / Oracle Linux
count_files
```

Звичайний запуск Jenkins:
```bash
docker-compose up -d
```

Перший запуск Jenkins:

```bash
docker-compose up -d jenkins-master
```

Далі відкрити http://localhost:8080, пройти початкове налаштування і створити вузол [agent-1](docs/readme-create-jenkins-agent.png).

```bash
echo "JENKINS_SECRET=<секрет agent-1>" > .env
docker-compose up -d
```

## Приклад виводу

```text
======================================
Підрахунок файлів у директорії /etc
======================================

Кількість звичайних файлів: 85
```

Число залежить від системи.

## Автор

Студент групи ПІ-241
