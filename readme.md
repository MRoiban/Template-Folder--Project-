This is a Python script that creates a project folder with the appropriate files and folders for different programming languages and frameworks.

## Usage
To use the script, navigate to the directory where the script is located and run the following command:

```
python create.py [options] [project_name]
```
## Options
-cpp
: Creates a C++ project
-p
 or 
-py
: Creates a Python project
-r
: Creates a React project
-gd
: Creates a Godot project
## Project Name
The project name is a required argument and should be entered after the option.

## File Structure
### C++ Project
```
./project
├── Class
├── Docs
└── Other
    ├── main.cpp
    └── makefile
```

### Python Project
```
./project
├── Class
├── Docs
└── Other
    └── [project_name].py
```
### React Project
```
./project
└── src
    ├── assets
    ├── components
    ├── screens
    ├── utils
    └── App.tsx
```
### Godot Project
```
./project
├── Assets
├── Controller
├── Model
├── Other
└── View
```