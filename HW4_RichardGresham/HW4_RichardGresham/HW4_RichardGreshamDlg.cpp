
// HW4_RichardGreshamDlg.cpp : implementation file
//

#include "pch.h"
#include "framework.h"
#include "HW4_RichardGresham.h"
#include "HW4_RichardGreshamDlg.h"
#include "afxdialogex.h"
#include <string>
#include <thread>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CAboutDlg dialog used for App About

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// Dialog Data
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_ABOUTBOX };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support

// Implementation
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(IDD_ABOUTBOX)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CHW4RichardGreshamDlg dialog



CHW4RichardGreshamDlg::CHW4RichardGreshamDlg(CWnd* pParent /*=nullptr*/)
	: CDialogEx(IDD_HW4_RICHARDGRESHAM_DIALOG, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CHW4RichardGreshamDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_EDIT_CHAT, m_edit1);
	DDX_Control(pDX, IDC_LIST1, m_listbox);

}

BEGIN_MESSAGE_MAP(CHW4RichardGreshamDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_EN_CHANGE(IDC_EDIT_CHAT, &CHW4RichardGreshamDlg::OnEnChangeEditChat)
	ON_BN_CLICKED(IDC_SEND, &CHW4RichardGreshamDlg::OnBnClickedSend)
	ON_LBN_SELCHANGE(IDC_LIST1, &CHW4RichardGreshamDlg::OnLbnSelchangeList1)
END_MESSAGE_MAP()


// CHW4RichardGreshamDlg message handlers

BOOL CHW4RichardGreshamDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != nullptr)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here

	//this is for sending
	localip.sin_family = AF_INET;
	inet_pton(AF_INET, srcIP, &localip.sin_addr.s_addr);
	localip.sin_port = htons(0);
	destination.sin_family = AF_INET;
	inet_pton(AF_INET, destIP, &destination.sin_addr.s_addr);
	destination.sin_port = htons(3514);
	send = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
	bind(send, (sockaddr*)&localip, sizeof(localip));



	//This is for receive
	local_receive.sin_family = AF_INET;
	inet_pton(AF_INET, srcIP, &local_receive.sin_addr.s_addr);
	local_receive.sin_port = htons(0);
	dest_receive.sin_family = AF_INET;
	inet_pton(AF_INET, destIP, &dest_receive.sin_addr.s_addr);
	dest_receive.sin_port = htons(3515);
	receive = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
	bind(receive, (sockaddr*)&dest_receive, sizeof(dest_receive));

	t1 = std::thread(&CHW4RichardGreshamDlg::receive_message, this);

	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CHW4RichardGreshamDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CHW4RichardGreshamDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CHW4RichardGreshamDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

 

void CHW4RichardGreshamDlg::OnEnChangeEditChat()
{
	
	// TODO:  If this is a RICHEDIT control, the control will not
	// send this notification unless you override the CDialogEx::OnInitDialog()
	// function and call CRichEditCtrl().SetEventMask()
	// with the ENM_CHANGE flag ORed into the mask.

	// TODO:  Add your control notification handler code here
	
}


void CHW4RichardGreshamDlg::OnBnClickedSend()
{
	//This happens upon being clicked
	CString chatMessage;
	m_edit1.GetWindowText(chatMessage);
	CString message = _T("I: ") + chatMessage;
	m_listbox.AddString(message);
	CT2A ct(chatMessage);
	std::string user_input(ct);
	user_input += "\0";
	const char* ch = user_input.c_str();
	sendto(send, ch, strlen(ch), 0, (sockaddr*)&destination, sizeof(destination));
	CString x;
	x.Empty();
	m_edit1.SetWindowText(x);

	
	

}

void CHW4RichardGreshamDlg::OnBnClickedCancel()
{
	//this closes my sockets upon the cancel button being sent to close the program.
	closesocket(send);
	closesocket(receive);
	t1.detach();
	CDialog::OnCancel();
}

void CHW4RichardGreshamDlg::OnLbnSelchangeList1()
{
	// TODO: Add your control notification handler code here
}
void CHW4RichardGreshamDlg::receive_message()
{
	while (true)
	{
		//this controls my message bock and what appears there.
		char buffer[128];
		struct sockaddr_in local_rec;
		int length = sizeof(struct sockaddr_in);
		int n = recvfrom(receive, buffer, 128, 0, (sockaddr*)&dest_receive, &length);
		CString str(buffer);
		CString str2(destIP);
		CString message = str2 + _T(": ") + str;
		m_listbox.AddString(message);


	}
}