loc="$2"
name="$1"

mkdir "$loc/$name" && cd "$loc/$name" &&
mkdir src include build &&
touch operw.toml README.md CHANGELOG.txt &&
touch src/main.c include/main.h &&

cat << EOF > src/main.c
#include "../include/main.h"

int main() {
    printf("Hello, World\n");
    return 0;
}
EOF

cat << EOF > include/main.h
#include <stdio.h>

int main();
EOF

cat << EOF > operw.toml
[build]
source = "src/main.c"
target = "build/a.out"

[test]
start = "build/./a.out"

[publish]

[install]
EOF