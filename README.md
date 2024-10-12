# AI Shorts

Social media content generator leveraging modern Generative AI tools to create revelant media content.

### **Installation**

1. **Clone the Repository**:

Begin by cloning the repository to your local machine:

```bash
git clone https://github.com/astronights/shorts-ai.git
cd shorts-ai
```

2. **Create a Python Virtual Environment**

It's recommended to create a virtual environment to keep your dependencies isolated:

```bash
python -m venv shorts
shorts\Scripts\activate  # For Windows
source shorts/bin/activate  # For macOS/Linux
```

3. **Install Dependencies**

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

4. **Set Up Jupyter** (Optional)

If you would like to run the notebooks, you can install the kernel in your environment.

   ```bash
   pip install jupyter notebook ipykernel python-dotenv
   ipython kernel install --user --name=shorts
   ```

## Starting the Server

1. **Run the Flask App**

Once all dependencies are installed, you can start the Flask server:

   ```bash
   flask --app api/index run -p 5328
   ```

This will start the Flask app on port `5328`, which you can access by navigating to `http://localhost:5328` in your browser.

