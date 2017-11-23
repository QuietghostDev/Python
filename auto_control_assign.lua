-- TODO Add default control writing
-- TODO Add control writing

-- Auto Control Assign v 0.4 script for FlyWithLua 2.6+
-- Nigel Hamilton


function generateDefaults()
	openFile(SCRIPT_DIRECTORY .. 'defaultControls.ctr', 'w')
end

function openFile(filename, mode)
	return io.open(filename, mode)
end

function button(str)
	if string.sub(str, 1, 3) == 'BTN' or string.sub(str, 1, 10) == '_joy_BUTN_' then
		return true
	else
		return false
	end
end

function axis(str)
	if string.sub(str, 1, 4) == 'AXIS' or string.sub(str, 1, 10) == '_joy_AXIS_' then
		return true
	else
		return false
	end
end

function loadControls(file)
	clear_all_axis_assignments()
	clear_all_button_assignments()
	for lines in file:lines() do
		if button(lines) then
			-- BTN joystickID.buttonID command
			local joystickID = tonumber(string.sub(lines, 5, string.find(lines, '.', 1, true)-1))
			local buttonID = tonumber(string.sub(lines, string.find(lines, '.', 1, true)+1, string.find(lines, ' ', 5, true)-1))
			local command = string.sub(lines, string.find(lines, ' ', 5, true)+1)
			
			set_button_assignment(joystickID + buttonID, command)
		end
		if axis(lines) then
			-- JOY axisID command, reverse
			local axisID = tonumber(string.sub(lines, 6, string.find(lines, ' ', 6, true)-1))
			local command = string.sub(lines, string.find(lines, ' ', 6, true)+1, string.find(lines, ',', 1, true)-1)
			local reverse = string.sub(lines, string.find(lines, ',', 1, true)+2)
			
			set_axis_assignment(axisID, command, reverse)
		end
	end
end

function controlIsValid(command)
	if command ~= 'sim/none/none' or command ~= 0 then
		return true
	else
		return false
	end
end

function getReverse(file, axis)
	for lines in file:lines() do
		if string.sub(lines, 14, string.find(lines, ' ')-1) == axis then
			if string.sub(lines, string.find(lines, ' ')+1) == '1' then
				return 'reverse'
			else
				return 'normal'
			end
		end
	end
end

function readControls(file, writeFile)
	local axisC = { "pitch", "roll", "yaw", "throttle", "collective", "left toe brake", "right toe brake", "prop",
	"mixture", "carb heat", "flaps", "thrust vector", "wing sweep", "speedbrakes", "displacement",
	"reverse", "elev trim", "ailn trim", "rudd trim", "throttle 1", "throttle 2", "throttle 3",
	"throttle 4", "prop 1", "prop 2", "prop 3", "prop 4", "mixture 1", "mixture 2",
	"mixture 3", "mixture 4", "reverse 1", "reverse 2", "reverse 3", "reverse 4", "landing gear",
	"nosewheel tiller", "backup throttle", "auto roll", "auto pitch", "view left/right", "view up/down", "view zoom" }
	for lines in file:lines() do
		if button(lines) then
			local buttonID = string.sub(lines, string.find(lines, '_use', 10, true)[-1]+1, string.find(lines, ' ', 10, true)-1)
			local command = string.sub(lines, string.find(lines, ' ', 10, true))
			if controlIsValid(command) and string.find(buttonID, '_desc', 14, true) == nil then
				writeButtonControl(writeFile, 0, buttonID, command)
			end
		end
		if axis(lines) then
			local axisID = string.sub(lines, string.find(lines, '_use', 10, true)[-1]+1, string.find(lines, ' ', 10, true)-1)
			local command = axisC[tonumber(string.sub(lines, string.find(lines, ' ', 10, true)))+1]
			local reverse = getReverse(file, axisID)
			writeAxisControl(writeFile, axisID, command, reverse)
		end
	end
end

function writeButtonControl(file, joystickID, buttonID, command)
	file:write('BTN ' .. joystickID .. '.' .. buttonID .. ' ' .. command .. '\n')
end

function writeAxisControl(file, axisID, command, reverse)
	file:write('AXIS ' .. axisID .. ' ' .. command .. ', ' .. reverse .. '\n')
end


file = openFile(AIRCRAFT_PATH .. 'controls.ctr', 'r')
if file ~= nil then
	loadControls(file)
	logMsg(string.format('FlyWithLua Info: %s assignments set.', PLANE_ICAO))
	print(string.format('FlyWithLua Info: %s assignments set.', PLANE_ICAO))
	file:close()
else
	logMsg('FlyWithLua Info: No controls found, loadind defaults.')
	print('FlyWithLua Info: No controls found, loadind defaults.')
	defaultControlFile = openFile(SCRIPT_DIRECTORY .. 'defaultControls.ctr')
	if defaultControlFile ~= nil then
		loadControls(defaultControlFile)
	else
		logMsg('FlyWithLua Error: No default control file found.')
		print('FlyWithLua Error: No default control file found.')
		generateDefaults()
end

print('Auto Control Assign: All controls loaded.')

-- function writeControls()
	-- file = openFile('X-Plane Joystick Settings.prf', 'r')
	-- if openFile(AIRCRAFT_PATH .. 'control.ctr') == nil then
		-- writeFile = openFile(AIRCRAFT_PATH .. 'controls.ctr', 'w')
		-- readControls(file, writeFile)
	-- end
-- end

-- do_on_exit('writeControls()')