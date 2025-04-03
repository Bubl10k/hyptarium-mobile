# hyptarium-mobile

## Prerequisites

- Python 3.10+
- pip
- NodeJs
- npm
- npx

## How to run

### Step 1: Clone the repository

```bash
  git clone https://github.com/Bubl10k/hyptarium-mobile.git
  cd hyptarium-mobile
```

### Step 2: Run the backend within another terminal

#### 1. Got to the backend folder and create and activate a virtual environment

```bash
   cd backend
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
```

#### 2. Install dependencies:

```bash
   pip install -r requirements.txt
```

#### 3. Running the Project

```bash
   uvicorn app.main:app --reload
```

### Step 3: Run the frontend within another terminal

#### 1. Install dependencies:

```bash
   npm install
```

#### 2. Run the project:

```bash
   npx expo start
```
