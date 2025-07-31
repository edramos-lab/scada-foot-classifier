# SCADA Foot Classifier

A distributed foot classification system using computer vision and machine learning, designed for industrial SCADA applications. The system consists of camera capture, inference processing, and web dashboard components.

## 🏗️ System Architecture

The project is composed of three main services:

### 1. Camera Publisher (`nano_cam_pub`)
- **Purpose**: Captures and publishes camera feed data
- **Target Device**: Jetson Nano
- **Base Image**: NVIDIA L4T Base (v2.0.2-r32.7.1)
- **Dependencies**: OpenCV, PyZMQ, NumPy
- **Network Mode**: Host

### 2. Inference & Storage (`xavier_infer_store`)
- **Purpose**: Runs foot classification inference and stores results
- **Target Device**: Jetson Xavier
- **Base Image**: NVIDIA L4T PyTorch (r35.3.1-pth2.0-py3)
- **Dependencies**: PyTorch, OpenCV, PyZMQ, SQLite
- **Features**: 
  - Loads pre-trained foot classification model (`foot_model.pt`)
  - Processes incoming camera data
  - Stores results in SQLite database (`foot_diagnostics.db`)

### 3. Web Dashboard (`laptop_ui`)
- **Purpose**: Provides web interface for viewing foot diagnostics
- **Target Device**: Laptop/Desktop
- **Base Image**: Python 3.10-slim
- **Dependencies**: Flask
- **Features**:
  - Web dashboard accessible on port 8000
  - Displays latest foot classification results
  - Serves processed images

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- For full system: Jetson Nano and Jetson Xavier devices
- For laptop dashboard only: Any system with Docker

### Running the Laptop Dashboard

To run just the web dashboard on your laptop:

```bash
# Navigate to project directory
cd scada-foot-classifier

# Run only the dashboard service
docker-compose up dashboard
```

The dashboard will be available at:
- **http://localhost:8000** - Main dashboard
- **http://localhost:8000/latest** - Latest foot classification image

### Running the Full System

To run all services (requires Jetson devices):

```bash
# Run all services
docker-compose up

# Run in background
docker-compose up -d

# Stop all services
docker-compose down
```

## 📁 Project Structure

```
scada-foot-classifier/
├── docker-compose.yml          # Service orchestration
├── laptop_ui/                  # Web dashboard service
│   ├── Dockerfile
│   └── app.py                  # Flask web application
├── nano_cam_pub/              # Camera publisher service
│   ├── Dockerfile
│   └── cam_pub.py             # Camera capture and publishing
└── xavier_infer_store/        # Inference and storage service
    ├── Dockerfile
    ├── infer_store.py          # Inference and database logic
    └── foot_model.pt           # Pre-trained foot classification model
```

## 🔧 API Endpoints

### Dashboard Endpoints

- `GET /` - Main dashboard page
- `GET /latest` - Returns the latest foot classification image

## 🗄️ Database Schema

The system uses SQLite database (`foot_diagnostics.db`) with the following schema:

```sql
CREATE TABLE foot_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    foot_type TEXT,
    image BLOB
);
```

## 🔄 Data Flow

1. **Camera Capture**: Jetson Nano captures camera feed
2. **Data Publishing**: Camera data published via ZMQ
3. **Inference**: Jetson Xavier receives data and runs classification
4. **Storage**: Results stored in SQLite database
5. **Visualization**: Laptop dashboard displays results via web interface

## 🛠️ Development

### Building Individual Services

```bash
# Build dashboard only
docker-compose build dashboard

# Build camera publisher
docker-compose build camera_pub

# Build inference service
docker-compose build infer_store
```

### Viewing Logs

```bash
# View all service logs
docker-compose logs

# View specific service logs
docker-compose logs dashboard
docker-compose logs camera_pub
docker-compose logs infer_store
```

## 🔍 Troubleshooting

### Common Issues

1. **Port 8000 already in use**:
   ```bash
   # Find process using port 8000
   sudo lsof -i :8000
   # Kill the process or change port in docker-compose.yml
   ```

2. **Database not found**:
   - Ensure the inference service has created the database
   - Check if `foot_model.pt` exists in `xavier_infer_store/`

3. **Camera access issues**:
   - Ensure camera permissions on Jetson Nano
   - Check camera device path in `cam_pub.py`

## 📊 Monitoring

- **Dashboard**: http://localhost:8000
- **Container Status**: `docker-compose ps`
- **Service Logs**: `docker-compose logs -f [service_name]`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
- Check the troubleshooting section above
- Review service logs for error messages
- Ensure all dependencies are properly installed 