import os

ALGORITHM = "Algorithms"
PERSONAL_INFO = "Personal Info"
TECHNOLOGY = "Technology"
PROGRAMMING = "Programming"
CLOUD = "Cloud"
PROJECT_MANAGEMENT = "Project Management"
HEALTH = "Health"
FITNESS = "Fitness"
LOGS = "Logs"
ROUTINE = "Routine"
BOOKS = "Books"
EDUCATION = "Education"
INDEX = "Index"
FINANCE = "Finance"
INVESTMENT = "Investment"
CULTURE = "Culture"
ENTERTAINMENT = "Entertainment"
SCIENCE = "Science"
DATA_PROCESSING = "Data Processing"
PHYSICS = "Physics"
PHILOSOPHY = "Philosophy"
WRITING = "Writing"
ART = "Art"
GENETICS = "Genetics"
HIGH_PERFORMANCE_COMPUTING = "High Performance Computing"
HETEROGENEOUS_PROGRAMMING = "Heterogeneous Programming"
GPGPU = "General Purpose GPU Programming"
LANGUAGES = "Language Learning"
LATIN = "Latin"
SPANISH = "Spanish"
RUSSIAN = "Russian"
SLOVAK = "Slovak"
ENGLISH = "English"
ESPERANTO = "Esperanto"
MINDFULNESS = "Mindfulness"
MSC = "Miscellaneous"
WORK = "Work"
DATA_SCIENCE = "Data science"
ARTIFICIAL_INTELLIGENCE = "Artificial Intelligence"
GARDENING = "Gardening"
DATABASES = "Databases"
PYTHON = "Python"
C = "C"
CPP = "C++"
CUDA = "Cuda"
BASH = "BASH"
SHELL = "Shell"
ZSH = "ZSH"
JAVA = "Java"
JAVASCRIPT = "JavaScript"
TYPESCRIPT = "TypeScript"
KOTLIN = "Kotlin"
RUST = "Rust (Programming language)"
RUBY = "Ruby (Programming language)"
GOLANG = "Golang"
ECOLOGY = "Ecology"
NEWS = "News"
QA = "Quality Assurance"
TESTING = "Testing"
UNIVERSITY = "University"
SECURITY = "Security"
BYRO = "Bureaucracy"
WEBDEV = "Web Development"
CSS = "CSS"
DEVOPS = "DevOps"
GIT = "Git"
IDEAS = "Ideas"
GAMES = "Games"
GAME_DEV = "Game Development"
HISTORY = "History"
LINUX = "Linux"
OS = "Operating System"
MATH = "Mathematics"
STAT = "Statistics"
ML = "Machine Learning"
PRIVACY = "Privacy"
PRODUCTIVITY = "Productivity"
JOURNALING = "Journaling"
PROMPTING = "Prompt Engineering"
PSYCHOLOGY = "Psychology"
RECIPES = "Recipes"
RPI = "Raspberry Pi"
SHOPPING = "Shopping"
SOFT_SKILLS = "Soft Skills"
SPEECH = "Rhetoric"
SURVIVAL = "Survival"
PREPPING = "Prepping"
MUSIC = "Music"
OUTDOORS = "Outdoors"
VIM = "Vim"
EDITOR = "Editor"
SOFTWARE = "Software"

categories = {
    "algorithm": [ALGORITHM],
    "address": [PERSONAL_INFO],
    "aws": [CLOUD, TECHNOLOGY, PROGRAMMING],
    "backlog": [PROJECT_MANAGEMENT, PERSONAL_INFO],
    "banglejs": [JAVASCRIPT, PROGRAMMING, TECHNOLOGY],
    "BASH": [PROGRAMMING],
    "bash": [PROGRAMMING],
    "beard": [HEALTH, ROUTINE],
    "book": [BOOKS, EDUCATION, CULTURE, ENTERTAINMENT],
    "c": [C, PROGRAMMING],
    "checklists": [PERSONAL_INFO, PROJECT_MANAGEMENT],
    "computers": [PROGRAMMING, TECHNOLOGY],
    "corona": [HEALTH],
    "crypto": [FINANCE, INVESTMENT],
    "cuda": [
        C,
        CPP,
        CUDA,
        PROGRAMMING,
        HIGH_PERFORMANCE_COMPUTING,
        GPGPU,
        HETEROGENEOUS_PROGRAMMING,
    ],
    "culture": [CULTURE],
    "dancing": [CULTURE, ENTERTAINMENT, ART],
    "datascience": [TECHNOLOGY, DATA_SCIENCE, SCIENCE, DATA_PROCESSING],
    "Emoji": [ENTERTAINMENT],
    "essays": [WRITING],
    "fonts": [ART, WRITING],
    "gemini": [TECHNOLOGY],
    "genetics": [SCIENCE, GENETICS],
    "index": [INDEX],
    "Kokkos": [
        CPP,
        GPGPU,
        PROGRAMMING,
        HETEROGENEOUS_PROGRAMMING,
        HIGH_PERFORMANCE_COMPUTING,
        DATA_PROCESSING,
    ],
    "Languages": [EDUCATION, LANGUAGES, INDEX],
    "lang": [EDUCATION, LANGUAGES],
    "la": [EDUCATION, LANGUAGES, LATIN],
    "logs": [PERSONAL_INFO, LOGS],
    "memos": [PERSONAL_INFO],
    "minfulness": [MINDFULNESS, ROUTINE, PHILOSOPHY, HEALTH],
    "nahodneBity": [MSC],
    "NESS": [WORK, PROGRAMMING, TECHNOLOGY],
    "Neural": [DATA_PROCESSING, ARTIFICIAL_INTELLIGENCE, DATA_SCIENCE],
    "physics": [SCIENCE, PHYSICS],
    "phys": [SCIENCE, PHYSICS],
    "plants": [GARDENING],
    "prisma": [
        JAVASCRIPT,
        TYPESCRIPT,
        PROGRAMMING,
        TECHNOLOGY,
        DATA_PROCESSING,
        DATABASES,
    ],
    "projects": [PROJECT_MANAGEMENT],
    "py": [PROGRAMMING, TECHNOLOGY, PYTHON],
    "python": [PROGRAMMING, TECHNOLOGY, PYTHON],
    "qa": [TESTING, QA],
    "quicknotes": [PERSONAL_INFO, MSC],
    "randomBits": [MSC],
    "rand": [MSC],
    "Ruby": [RUBY, PROGRAMMING, TECHNOLOGY],
    "Rust": [RUST, PROGRAMMING, TECHNOLOGY],
    "self_care": [HEALTH],
    "shopping": [MSC],
    "SWF": [MSC],
    "tensorflow": [PROGRAMMING, ARTIFICIAL_INTELLIGENCE],
    "TensorFlow": [PROGRAMMING, ARTIFICIAL_INTELLIGENCE],
    "todo": [PROJECT_MANAGEMENT, PERSONAL_INFO],
    "unicode": [TECHNOLOGY],
    "uni": [EDUCATION, UNIVERSITY],
    "want": [LOGS, PERSONAL_INFO],
    "weight": [LOGS, PERSONAL_INFO],
    "work": [WORK],
    "zero": [ECOLOGY],
    "ZSH": [SHELL, ZSH, PROGRAMMING, TECHNOLOGY],
    "javascript": [JAVASCRIPT, WEBDEV, PROGRAMMING, TECHNOLOGY],
    "typescript": [TYPESCRIPT, WEBDEV, JAVASCRIPT, PROGRAMMING, TECHNOLOGY],
    "kotlin": [KOTLIN, JAVA, PROGRAMMING, TECHNOLOGY],
    "java": [JAVA, PROGRAMMING, TECHNOLOGY],
    "cpp": [CPP, PROGRAMMING, TECHNOLOGY],
    "appsec": [SECURITY, PROGRAMMING, TECHNOLOGY],
    "byro": [BYRO],
    "css": [CSS, WEBDEV, PROGRAMMING, TECHNOLOGY],
    "db": [DATABASES, PROGRAMMING, TECHNOLOGY],
    "devops": [WEBDEV, PROGRAMMING, TECHNOLOGY, DEVOPS],
    "git": [GIT, PROGRAMMING, TECHNOLOGY, SOFTWARE],
    "en": [EDUCATION, LANGUAGES, ENGLISH],
    "eo": [EDUCATION, LANGUAGES, ESPERANTO],
    "sp": [EDUCATION, LANGUAGES, SPANISH],
    "ru": [EDUCATION, LANGUAGES, RUSSIAN],
    "thoughts": [PERSONAL_INFO, IDEAS],
    "gamedev": [GAME_DEV, GAMES, PROGRAMMING, TECHNOLOGY],
    "golang": [GOLANG, PROGRAMMING, TECHNOLOGY],
    "history": [HISTORY, EDUCATION],
    "latex": [WRITING, PROGRAMMING],
    "linux": [LINUX, OS, TECHNOLOGY],
    "math": [MATH, SCIENCE],
    "stat": [MATH, SCIENCE, STAT],
    "ML": [ML, DATA_SCIENCE, ARTIFICIAL_INTELLIGENCE, STAT],
    "msc": [MSC],
    "music": [ART, ENTERTAINMENT, MUSIC],
    "philosophy": [EDUCATION, PHILOSOPHY],
    "plans": [PROJECT_MANAGEMENT, PERSONAL_INFO, LOGS],
    "privacy": [PRIVACY, SECURITY, PERSONAL_INFO],
    "productivity": [PRODUCTIVITY, WORK],
    "programs": [TECHNOLOGY, SOFTWARE],
    "software": [TECHNOLOGY, SOFTWARE],
    "programming": [PROGRAMMING, TECHNOLOGY],
    "prompting": [ARTIFICIAL_INTELLIGENCE, PROMPTING, DATA_SCIENCE],
    "psychology": [HEALTH, PSYCHOLOGY],
    "recipes": [RECIPES],
    "research": [SCIENCE, PERSONAL_INFO, LOGS],
    "rpi": [RPI, TECHNOLOGY],
    "ideas": [IDEAS],
    "science": [EDUCATION, SCIENCE],
    "security": [SECURITY],
    "shopping": [SHOPPING, PERSONAL_INFO],
    "soft_skills": [SOFT_SKILLS],
    "speech": [SPEECH, SOFT_SKILLS],
    "survival": [SURVIVAL, PREPPING, OUTDOORS],
    "vim": [SOFTWARE, TECHNOLOGY, EDITOR],
    "webdev": [WEBDEV, PROGRAMMING, TECHNOLOGY],
    "writing": [WRITING],
    "journaling": [WRITING, JOURNALING],
}


def get_tags(filename):
    _, file = os.path.split(filename)

    filename_parts = file.replace(".wiki", "").replace(".md", "").split("_")
    tags = set()

    print(f"fileparts: {filename_parts}")

    for part in filename_parts:
        if part in categories:
            tags.update(categories[part])

    return list(tags)


if __name__ == "__main__":
    test_cases = [
        "Kokkos.wiki",
        "msc_ideas.wiki",
        "writing_journaling_like_a_stoic.wiki",
        "math_stat_statistical_tests.wiki",
        "cuda_kernels.wiki",
        "index.wiki",
        "physics_index.wiki",
        "phys_IM_index.wiki",
    ]

    for test in test_cases:
        print(f"{test} ---> {get_tags(test)}")
