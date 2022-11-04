on run
	-- activate application "Google Chrome"
    tell application "System Events"
        tell menu 1 of menu bar item "??????" of menu bar 1 of application process "Google Chrome"
            every UI element
        end tell
    end tell
end run