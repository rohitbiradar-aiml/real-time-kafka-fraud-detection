# real-time-kafka-fraud-detection

# Real-Time Kafka Fraud Detection System

## Project Overview

The **Real-Time Kafka Fraud Detection System** is a real-time financial transaction monitoring solution developed using Python, Apache Kafka, Pandas, and Streamlit.

The system simulates financial transactions, streams transaction data through Apache Kafka, and processes incoming events to identify potentially fraudulent activities using a rule-based detection mechanism.

An interactive Streamlit dashboard provides real-time transaction monitoring, fraud alerts, and analytical insights, enabling users to track transaction activity and suspicious patterns efficiently.

## Key Features

- **Real-Time Data Streaming:** Processes financial transaction events using Apache Kafka.
- **Transaction Generation:** Generates simulated financial transactions using a Python-based producer.
- **Event Processing:** Uses a Kafka consumer to continuously receive and process incoming transactions.
- **Fraud Detection:** Identifies suspicious transactions using configurable rule-based detection logic.
- **Automated Fraud Alerts:** Flags transactions exceeding the predefined threshold of $1,000.
- **Interactive Dashboard:** Displays live transaction activity and fraud detection results using Streamlit.
- **Transaction Analytics:** Provides insights into transaction volumes, amounts, and fraud rates.
- **Data Visualization:** Presents transaction trends, fraud statistics, and transaction status through interactive charts.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Streaming Platform | Apache Kafka |
| Kafka Integration | Confluent Kafka Python |
| Data Processing | Pandas |
| Dashboard | Streamlit |
| Containerization | Docker, Docker Compose |
| Detection Method | Rule-Based Fraud Detection |

## System Architecture

The application follows a producer-consumer architecture to process financial transactions in real time.

**1. Transaction Producer**

Generates simulated financial transaction records and publishes them to a Kafka topic.

**2. Apache Kafka**

Acts as the distributed event-streaming platform, handling transaction messages between the producer and consumer.

**3. Transaction Consumer**

Consumes incoming Kafka messages, processes transaction data, and applies rule-based fraud detection logic to identify suspicious transactions.

**4. Streamlit Dashboard**

Displays transaction records, fraud alerts, transaction statistics, and visual analytics through an interactive dashboard.

### Data Flow

```text
Transaction Generator
        |
        v
   Kafka Producer
        |
        v
   Apache Kafka
        |
        v
   Kafka Consumer
        |
        v
  Fraud Detection
        |
        v
 Streamlit Dashboard
        |
        v
 Live Analytics & Alerts
```

## Project Structure

```text
real-time-kafka-fraud-detection/
│
├── producer.py
├── consumer.py
├── app.py
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd real-time-kafka-fraud-detection
```

### 2. Install Dependencies

```bash
pip install confluent-kafka pandas streamlit
```

### 3. Start Apache Kafka

Ensure Docker is installed and running, then execute:

```bash
docker compose up -d
```

### 4. Start the Kafka Consumer

Open a terminal and run:

```bash
python consumer.py
```

### 5. Start the Transaction Producer

Open another terminal and execute:

```bash
python producer.py
```

### 6. Launch the Streamlit Dashboard

Open a separate terminal and run:

```bash
streamlit run app.py --server.address 0.0.0.0
```

The dashboard can then be accessed through the local Streamlit URL displayed in the terminal.

## Fraud Detection Logic

The system uses a rule-based approach to identify potentially suspicious financial transactions.

- Transactions exceeding the predefined threshold of **$1,000** are flagged for review.
- Incoming transaction events are continuously monitored by the Kafka consumer.
- Suspicious transactions are identified and reflected in the dashboard.
- Transaction statistics and fraud rates are presented through visual analytics.

## Learning Outcomes

This project demonstrates practical implementation of real-time data engineering and stream-processing concepts, including:

- Understanding Apache Kafka architecture and event streaming.
- Building Kafka producers and consumers using Python.
- Processing real-time financial transaction data.
- Implementing rule-based fraud detection mechanisms.
- Integrating Kafka with Python data-processing workflows.
- Developing interactive dashboards using Streamlit.
- Visualizing transaction patterns and fraud statistics.
- Using Docker to manage application infrastructure.

## Future Enhancements

- Integrate Machine Learning models for intelligent fraud detection.
- Implement anomaly detection for identifying unusual transaction patterns.
- Introduce transaction velocity checks and customer-based risk scoring.
- Store transaction history in a persistent database.
- Add configurable fraud detection rules.
- Implement advanced monitoring and alerting mechanisms.

## Disclaimer

This project uses simulated financial transaction data and a rule-based fraud detection approach with a predefined transaction threshold. It is intended for educational and demonstration purposes only and is not designed for production financial monitoring or real-world fraud prevention.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

**Rohit Biradar**

Data Scientist | AI/ML & Data Engineering Enthusiast
