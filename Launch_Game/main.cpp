#include <Windows.h>
#include <string>
using namespace std;
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) 
{
    STARTUPINFOA si;
    PROCESS_INFORMATION pi;

    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory(&pi, sizeof(pi));
    // Specify the application to launch (e.g., Notepad)
    // You can also provide the full path if the application is not in a standard location or your PATH.
    LPCSTR lpApplicationName = "SDBHeroes_WorldMission.exe"; //Steam Version!!!
    if (!CreateProcessA(
        lpApplicationName,    // Application name
        (LPSTR)L"",        // Command line
        NULL,                 // Process security attributes
        NULL,                 // Thread security attributes
        FALSE,                // Inherit handles
        0,                    // Creation flags
        NULL,                 // New environment block
        NULL,                 // Current directory
        &si,                  // STARTUPINFO structure
        &pi                   // PROCESS_INFORMATION structure
    )) 
    {
        MessageBoxA(0, "Failed to Run SDBHeroes_WorldMission.exe", "SDBHeroes-AntiEACLauncher", MB_OK | MB_ICONWARNING);
        return EXIT_FAILURE;
    }
    else {
        return EXIT_SUCCESS;
    }
	return 0;
}