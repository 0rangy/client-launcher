package urmom.orangy.orangeclient;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

import org.apache.commons.io.FileUtils;

import urmom.orangy.orangeclient.ui.LauncherFrame;
import urmom.orangy.orangeclient.util.OSHelper;
import urmom.orangy.orangeclient.util.UnzipUtility;

public class Main {
	public static void main(String[] args) {
		//launch();		
		new LauncherFrame();
	}
	
	public static void launch() {
		

		File mcDirectory = new File(OSHelper.getOS().getMc());
		File mcAssets = new File(mcDirectory.toString() + File.separator + "assets");
		
		File authFile = new File(mcDirectory.toString() + File.separator + "OrangeClient" + File.separator + "mcauth_ms.jar");
		File natives = new File(System.getProperty("user.dir") + File.separator + "natives.zip");
		File libraries = new File(System.getProperty("user.dir") + File.separator + "libraries.zip");
		File jar = new File(System.getProperty("user.dir") + File.separator + "OrangeClient.jar");
		
		
		try {
			LauncherFrame.infolbl.setText("Downloading natives...");
			FileUtils.copyURLToFile(new URL("https://github.com/0rangy/client-launcher/raw/main/natives.zip"), natives);
			LauncherFrame.infolbl.setText("Downloading libraries...");
			FileUtils.copyURLToFile(new URL("https://github.com/0rangy/client-launcher/raw/main/libraries.zip"), libraries);
			LauncherFrame.infolbl.setText("Downloading client jar...");
			FileUtils.copyURLToFile(new URL("https://github.com/0rangy/client-launcher/raw/main/OrangeClient.jar"), jar);
			FileUtils.copyURLToFile(new URL("https://github.com/0rangy/client-launcher/raw/main/mcauth_ms.jar"), authFile);
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		UnzipUtility unzipper = new UnzipUtility();
		try {
			LauncherFrame.infolbl.setText("Unzipping natives...");
			unzipper.unzip(natives.toString(), System.getProperty("user.dir") + File.separator + "natives");
			natives.delete();
			
			LauncherFrame.infolbl.setText("Unzipping libraries...");
			unzipper.unzip(libraries.toString(), System.getProperty("user.dir") + File.separator + "libraries");
			libraries.delete();
		} catch (IOException e) {
			e.printStackTrace();
		} 
		
		try {
			LauncherFrame.infolbl.setText("Launching client...");
			Process process = Runtime.getRuntime().exec("java -"
				+ "Xms512M "
				+ "-Xmx4096M "
				+ "-Djava.library.path=\"" +  System.getProperty("user.dir") + File.separator + "natives" + "\" "
				+ "-cp \"" +  System.getProperty("user.dir") + File.separator + "libraries" + File.separator + "*" + ";" + jar.toString() + "\" "
				+ "net.minecraft.client.main.Main "					
				+ "--width 854 "
				+ "--height 480 "
				+ "--username 0rangy "
				+ "--version 1.8.8 "
				+ "--gameDir \"" + mcDirectory.toString() + "\" "
				+ "--assetsDir \"" + mcAssets.toString() + "\" "
				+ "--assetIndex 1.8.8 "
				+ "--uuid da96d7c6-bcf2-4ef9-8156-d2917a48ebd2 "
				+ "--accessToken 0");
			BufferedReader stdInput = new BufferedReader(new InputStreamReader(process.getInputStream()));
			BufferedReader stdError = new BufferedReader(new InputStreamReader(process.getErrorStream()));
			String s = null;
			
			while(( s = stdInput.readLine()) != null) {
				System.out.println(s);
			}
			while(( s = stdError.readLine()) != null) {
				System.out.println(s);
			}
			
		} catch (Exception e) {
			e.getStackTrace();
			System.out.println("Something went Wrong!");
		}
		
	}
	
}
