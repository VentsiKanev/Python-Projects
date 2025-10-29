from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

app = Flask(__name__)

# --- Database Config ---
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root1337434@localhost/DiaryProgram"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# --- Reflect existing tables safely ---
# REFLECTED TABLE


with app.app_context():
    class Reflector(db.Model):
        __tablename__ = "Person"
        __table_args__ = {"autoload_with": db.engine}

        # Helper to convert row to dict
        def to_dict(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# --- Helper function to convert row to dict ---
def to_dict(obj):
    return obj.to_dict()
    
    # Optional: Inspect columns
    #inspector = inspect(db.engine)
    #columns = inspector.get_columns("person")
    #print("Columns in 'person' table:")
    #for col in columns:
       #print(f"- {col['name']} ({col['type']})")

    

# Get all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    todos = db.session.query(Reflector).all()
    return jsonify([to_dict(t) for t in todos])

# Get single todo
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = db.session.query(Reflector).get(todo_id)
    if todo:
        return jsonify(to_dict(todo))
    return jsonify({"error": "Todo not found"}), 404

# Create todo
@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    todo = Reflector(**data)  # keys in JSON must match column names
    db.session.add(todo)
    db.session.commit()
    return jsonify(to_dict(todo)), 201

# Update todo
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = db.session.query(Reflector).get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json()
    for key, value in data.items():
        if hasattr(todo, key):
            setattr(todo, key, value)

    db.session.commit()
    return jsonify(to_dict(todo))

# Delete todo
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = db.session.query(Reflector).get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    db.session.delete(todo)
    db.session.commit()
    return "", 204

# --- Run App ---
if __name__ == "__main__":
    app.run(debug=True)

