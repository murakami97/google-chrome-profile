on run name
    tell application "System Events"
        tell menu 1 of menu bar item "??????" of menu bar 1 of application process "Google Chrome"
            tell menu item (name as string)
                click
            end tell
        end tell
    end tell
end run