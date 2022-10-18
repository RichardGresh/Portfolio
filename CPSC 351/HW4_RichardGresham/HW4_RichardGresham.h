
// HW4_RichardGresham.h : main header file for the PROJECT_NAME application
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'pch.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols


// CHW4RichardGreshamApp:
// See HW4_RichardGresham.cpp for the implementation of this class
//

class CHW4RichardGreshamApp : public CWinApp
{
public:
	CHW4RichardGreshamApp();

// Overrides
public:
	virtual BOOL InitInstance();

// Implementation

	DECLARE_MESSAGE_MAP()
};

extern CHW4RichardGreshamApp theApp;
