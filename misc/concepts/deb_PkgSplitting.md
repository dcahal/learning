# Debian Package Splitting
### (for KDE Neon)

A change to a source package can add new components which should be spun off as their own package/dependency. The easiest way to recognize this is when the build fails:

```
09:51:12 Failure: test_listmissing_errors(Lint::TestLog):
09:51:12   usr/lib/x86_64-linux-gnu/qt5/qml/org/kde/syntaxhighlighting/libkquicksyntaxhighlightingplugin.so
09:51:12   usr/lib/x86_64-linux-gnu/qt5/qml/org/kde/syntaxhighlighting/qmldir
```

If you get this error near the end of the build log, the "missing" files need to be declared as a separate package with a new `.install` file in `debian/`. For the example above, that would be `qml-module-org-kde-syntaxhighlighting`.

# New QML modules for KDE Frameworks

When many build jobs for Kirigami or QML apps begin to fail on a missing KDE Frameworks component, it may be because the Frameworks library needs a new QML module. This is a three step process:

1. Add QtQuick as a build time dependency for the Frameworks component in question.
    * `qtdeclarative5-dev` in Debian
2. Check if the build fails with missing files
3. Create a new `.install` file in `debian/`
4. Add package description for the new module to `control`
5. Wait for the Frameworks package to build again
6. Add the new QML module as a **runtime dependency** for the app which produced the original error (missing Frameworks component)
