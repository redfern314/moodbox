//
//  MoodBoxViewController.h
//  MoodBox
//
//  Created by Trung Le on 6/29/13.
//  Copyright (c) 2013 moodbox. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface MoodBoxViewController : UIViewController
<NSURLConnectionDelegate>
{
    IBOutlet UIActivityIndicatorView *activityIndicator;
    IBOutlet UIImageView *logoImage;
    IBOutlet UIButton *tanButton;
    IBOutlet UIButton *cyanButton;
    IBOutlet UIButton *greenButton;
    IBOutlet UIButton *pinkButton;
    IBOutlet UIButton *purpleButton;
    IBOutlet UIButton *blueButton;
    
    IBOutlet UIButton *wakeupButton;
    IBOutlet UIButton *refreshedButton;
    IBOutlet UIButton *focusedButton;
    IBOutlet UIButton *chillButton;
    IBOutlet UIButton *partyButton;
    IBOutlet UIButton *sexyButton;
    
    IBOutlet UIButton *workButton;
    
    IBOutlet UIImageView *wantImage;
    IBOutlet UIImageView *howImage;
}

@property (nonatomic, strong) NSURLConnection *urlConnection;
@property (nonatomic, strong) NSMutableData *responseData;

- (IBAction)setMoodTan:(id)sender;
- (IBAction)setMoodCyan:(id)sender;
- (IBAction)setMoodGreen:(id)sender;
- (IBAction)setMoodPurple:(id)sender;
- (IBAction)setMoodPink:(id)sender;
- (IBAction)setMoodBlue:(id)sender;
- (IBAction)setMoodRed:(id)sender;

@end
