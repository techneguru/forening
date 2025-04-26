# Båtforening Project

## Overview
This project manages a boat association's operations, including:
- A public-facing website.
- A members' area for accessing documents, member lists, and submitting expenses.
- Automated invoicing using Python.

## Prerequisites
- Ubuntu 20.04 or later.
- Docker and Docker Compose installed.
- Python 3.11 (for backend proxy development, if needed).

## Setup Instructions

sudo apt update
sudo apt install -y docker.io docker-compose python3-pip

### 1. Clone the Repository
```bash
git clone https://github.com/techneguru/forening.git
cd techneguru/forening

2. Configure Environment Variables
Create a .env file in the root directory:
cp .env.example .env
nano .env  # Update credentials as needed

3. Install Docker and Docker Compose
Install Docker:
sudo apt install -y docker-compose
docker-compose up --build -d

4. Build and Run the Project
Run the following command to start all services:
docker-compose up --build -d

5. Access the Application
Public Website: http://<your-server-ip>
Members' Area: http://<your-server-ip>/andelseier
NocoDB Admin: http://<your-server-ip>:8080

6. Stopping the Services
To stop all services, run:

docker-compose down

### 7. Install Python Dependencies (Optional)
If you need to run the backend proxy locally, install the required Python packages:
```bash
pip install -r [requirements.txt](http://_vscodecontentref_/20)

Notes
Ensure the .env file is not exposed publicly.
Use a strong MYSQL_ROOT_PASSWORD and NC_AUTH_JWT_SECRET for production.
Regularly back up the db_data and noco_data volumes.

Troubleshooting
Check logs for errors
docker-compose logs

Ensure all services are healthy:
docker ps

### 8. Configure NocoDB Authentication
1. Access the NocoDB admin interface: `http://<your-server-ip>:8080`.
2. Log in with the default admin account or create a new admin user.
3. Create roles (e.g., "Admin", "Member") and assign permissions for tables and views.
4. Add user accounts for members and assign them the "Member" role.

### 9. Backup and Restore
#### Backup
To back up the database, run:
```bash
docker exec -t <db_container_name> mysqldump -u<MYSQL_USER> -p<MYSQL_PASSWORD> <MYSQL_DATABASE> > backup.sql

RESTORE BACKUP
docker exec -i <db_container_name> mysql -u<MYSQL_USER> -p<MYSQL_PASSWORD> <MYSQL_DATABASE> < backup.sql