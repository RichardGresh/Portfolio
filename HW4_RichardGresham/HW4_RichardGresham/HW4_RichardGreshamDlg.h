
// HW4_RichardGreshamDlg.h : header file
//
#include <thread>
#pragma once


// CHW4RichardGreshamDlg dialog
class CHW4RichardGreshamDlg : public CDialogEx
{
// Construction
public:
	CHW4RichardGreshamDlg(CWnd* pParent = nullptr);	// standard constructor

// Dialog Data
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_HW4_RICHARDGRESHAM_DIALOG };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support


// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
public:
	sockaddr_in destination;
	sockaddr_in dest_receive;
	sockaddr_in local_receive;
	sockaddr_in localip;
	void receive_message();
	afx_msg void OnEnChangeEditChat();
	afx_msg void OnBnClickedSend();
	CEdit m_edit1;
	SOCKET send;
	SOCKET receive;
	const char* srcIP = "127.0.0.1";
	const char* destIP = "127.0.0.1";
	
	std::thread t1;
	afx_msg void OnLbnSelchangeList1();
	CListBox m_listbox;
	afx_msg void OnBnClickedCancel();
	
};
