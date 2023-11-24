import cx_Freeze

executables = [
    cx_Freeze.Executable (script="space.py", icon = "logo.ico")
]

cx_Freeze.setup (
    name = "Space Mark",
    options ={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["space.jpg",
                              "space.png",
                              "space.mp3",
                              "Space.txt"
                              ]
        }
    }, executables = executables
)