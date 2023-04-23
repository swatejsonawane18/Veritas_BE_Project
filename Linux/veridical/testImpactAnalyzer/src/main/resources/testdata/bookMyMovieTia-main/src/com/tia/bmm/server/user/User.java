package com.tia.bmm.server.user;

public class User {
	int userId;
    String name;
    String mobNo;
    private String emailId;
    String sex;

    public User() {}

    User(int uid, String n, String mno, String eid, String gen) {
        userId = uid;
        name = n;
        mobNo = mno;
        setEmailId(eid);
        sex = gen;
    }

	public String getEmailId() {
		return emailId;
	}

	public void setEmailId(String emailId) {
		this.emailId = emailId;
	}
}
