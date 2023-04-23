package com.pict.tia.core;
import java.io.IOException;
import java.util.List;

import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

import com.pict.tia.api.JiraAPIRequest;
import com.pict.tia.constants.TIAConstants;
import com.pict.tia.mocks.jiracommits.JiraServiceMock;
import com.pict.tia.utils.MockServerUtils;
import com.pict.tia.utils.ProcessUtils;

public class DependencyFinder {

	private static final Logger logger = LogManager.getLogger(DependencyFinder.class);
	public static void main(String[] arg) throws IOException
	{
	}
	public int findDependencies() throws IOException{
		MockServerUtils.startMockServer();
		JiraServiceMock mockService = new JiraServiceMock();
		String inputJira = "1428623";
		mockService.mockGetCommitsAPI(inputJira, 200);
		JiraAPIRequest jira = new JiraAPIRequest();
		List<String> commitList = jira.getAllCommitsFromJira(inputJira);
		logger.info("List Commits: "+commitList);
		MockServerUtils.stopMockServer();
		try
		{
			return ProcessUtils.executePYDrillerScriptForFunctionDependency(TIAConstants.DOXYGEN_OUTPUT_REPORT);
		}
		catch (IOException e)
		{
			logger.error("Error occurred while executing pydriller");
		}
		return -1;
	}

}
