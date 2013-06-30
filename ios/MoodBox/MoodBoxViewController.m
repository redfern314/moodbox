//
//  MoodBoxViewController.m
//  MoodBox
//
//  Created by Trung Le on 6/29/13.
//  Copyright (c) 2013 moodbox. All rights reserved.
//

#import "MoodBoxViewController.h"

#define SERVER_IP_ADDRESS @"http://192.168.1.114:8080"

@interface MoodBoxViewController ()

@end

@implementation MoodBoxViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.

    [logoImage setAlpha:0.0];
    [activityIndicator stopAnimating];
}

- (void)viewDidAppear:(BOOL)animated
{
    [UIImageView animateWithDuration:1.0
                          animations:^{
                              [logoImage setAlpha:1.0];
                          }];
    
    [self connecting];
    [self get];
    
//    [NSTimer scheduledTimerWithTimeInterval:3 target:self selector:@selector(didConnect:) userInfo:nil repeats:NO];

}

- (void)connecting
{
    [activityIndicator startAnimating];
    
    [tanButton setAlpha:0.0];
    [greenButton setAlpha:0.0];
    [cyanButton setAlpha:0.0];
    [pinkButton setAlpha:0.0];
    [purpleButton setAlpha:0.0];
    [blueButton setAlpha:0.0];
    
    [wakeupButton setAlpha:0.0];
    [refreshedButton setAlpha:0.0];
    [chillButton setAlpha:0.0];
    [focusedButton setAlpha:0.0];
    [partyButton setAlpha:0.0];
    [sexyButton setAlpha:0.0];

    [workButton setAlpha:0.0];
    
    [wantImage setAlpha:0.0];
    [howImage setAlpha:0.0];

    [UIImageView animateWithDuration:1.0
                          animations:^{
                              [logoImage setCenter:CGPointMake(logoImage.center.x                                                                                  , self.view.bounds.size.height / 2)];}];

}

- (void)didConnect:(NSTimer*)timer
{
    [activityIndicator stopAnimating];
    
    [self buttonFadeIn:tanButton];
    [self buttonFadeIn:greenButton];
    [self buttonFadeIn:cyanButton];
    [self buttonFadeIn:pinkButton];
    [self buttonFadeIn:purpleButton];
    [self buttonFadeIn:blueButton];
    
    [self buttonFadeIn:wakeupButton];
    [self buttonFadeIn:refreshedButton];
    [self buttonFadeIn:chillButton];
    [self buttonFadeIn:focusedButton];
    [self buttonFadeIn:partyButton];
    [self buttonFadeIn:sexyButton];
    
    [self buttonFadeIn:workButton];
 
    [UIImageView animateWithDuration:1.0
                       animations:^{
                           [wantImage setAlpha:1.0];}];
    
    [UIImageView animateWithDuration:1.0
                          animations:^{
                              [howImage setAlpha:1.0];}];
    
    
    [UIImageView animateWithDuration:1.0
                          animations:^{
                              double shrunkWidth = logoImage.frame.size.width * .8;
                              double shrunkHeight = logoImage.frame.size.height * .8;
                              [logoImage setFrame:CGRectMake((self.view.frame.size.width / 2 - shrunkWidth / 2),                                                                                  -130, shrunkWidth, shrunkHeight)];
                              
                          }];

}

- (void)buttonFadeIn:(UIButton*)button
{
    [UIButton animateWithDuration:1.0
                       animations:^{
                           [button setAlpha:1.0];}];
    
}

- (void)get
{
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:SERVER_IP_ADDRESS]];
    
    NSOperationQueue *queue = [[NSOperationQueue alloc] init];

    [NSURLConnection sendAsynchronousRequest:request
                                       queue:queue
                           completionHandler:^(NSURLResponse *response, NSData *data, NSError *error) {
                               
                               if (!error) {
                                   NSString *responseString = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
                                   
                                   NSLog(@"%@", responseString);
                                   
                                   [self didConnect:nil];
                               } else {
                                   NSLog(@"Error: %@ with data %@", error, data);
                               }
                           }];
}

- (void)post:(NSString*)stringData
{
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:SERVER_IP_ADDRESS]];
    request.HTTPMethod = @"POST";
    
    // This is how we set header fields
    [request setValue:@"application/xml; charset=utf-8" forHTTPHeaderField:@"Content-Type"];
    
    // Convert your data and set your request's HTTPBody property
    NSData *requestBodyData = [stringData dataUsingEncoding:NSUTF8StringEncoding];
    request.HTTPBody = requestBodyData;
    
    NSOperationQueue *queue = [[NSOperationQueue alloc] init];
    
    [NSURLConnection sendAsynchronousRequest:request
                                    queue:queue
                        completionHandler:^(NSURLResponse *response, NSData *data, NSError *error) {
                            
                            if (!error) {
                                NSString *responseString = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
                                
                                NSLog(@"%@", responseString);
                                
                            } else {
                                NSLog(@"Error: %@ with data %@", error, data);
                            }
                        }];
    
    
    
}

#pragma  mark Button actions

- (IBAction)setMoodTan:(id)sender
{
    [self post:@"setMood:TAN"];
}

- (IBAction)setMoodCyan:(id)sender
{
    [self post:@"setMood:CYAN"];
}

- (IBAction)setMoodGreen:(id)sender
{
    [self post:@"setMood:GREEN"];
}

- (IBAction)setMoodPink:(id)sender
{
    [self post:@"setMood:PINK"];
}

- (IBAction)setMoodPurple:(id)sender
{
    [self post:@"setMood:PURPLE"];
}

- (IBAction)setMoodBlue:(id)sender
{
    [self post:@"setMood:BLUE"];
}

- (IBAction)setMoodRed:(id)sender
{
    [self post:@"setMood:RED"];
}


#pragma mark NSURLConnectionDelegate

- (void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response {
    // A response has been received, this is where we initialize the instance var you created
    // so that we can append data to it in the didReceiveData method
    // Furthermore, this method is called each time there is a redirect so reinitializing it
    // also serves to clear it
    self.responseData = [[NSMutableData alloc] init];
}

- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data {
    // Append the new data to the instance variable you declared
    [self.responseData appendData:data];
}

- (NSCachedURLResponse *)connection:(NSURLConnection *)connection
                  willCacheResponse:(NSCachedURLResponse*)cachedResponse {
    // Return nil to indicate not necessary to store a cached response for this connection
    return nil;
}

- (void)connectionDidFinishLoading:(NSURLConnection *)connection {
    // The request is complete and data has been received
    // You can parse the stuff in your instance variable now

    NSString *responseString = [[NSString alloc] initWithData:self.responseData encoding:NSUTF8StringEncoding];
    
    NSLog(@"%@", responseString);
    
    [self didConnect:nil];

}

- (void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error {
    // The request has failed for some reason!
    // Check the error var
}

@end
