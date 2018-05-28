//
//  IMKSampleController.m
//  IMKSample
//
//  Created by palance on 17/3/22.
//  Copyright © 2017年 palanceli. All rights reserved.
//

#import "IMKSampleController.h"
#import "SGDXIMEngine.h"
#import "IMKSCandidatesWindow.h"

static WordsLibManger *manger;


@implementation IMKSampleController
{
  IMKSCandidatesWindow* _candidatesWindow;
}
-(IMKSCandidatesWindow*) candidatesWindow
{
  
  if(_candidatesWindow == nil){
      
      // 只执行一次
      manger = [[WordsLibManger alloc] init];
      [manger getWordsLib];
      
    _candidatesWindow = [[IMKSCandidatesWindow alloc]
               initWithContentRect:NSZeroRect
               styleMask:NSBorderlessWindowMask
               backing:NSBackingStoreBuffered
               defer:YES];
  }
  return _candidatesWindow;
}

-(void) appendComposedString:(NSString*) string client:(id)sender
{
  SGDXIMEngine* imEngine = [SGDXIMEngine sharedObject];
//  NSString *compString = [imEngine appendComposeString:string];
    manger.pinyin = [NSString stringWithFormat:@"%@%@", manger.pinyin, string];
    
    NSString * pin = manger.pinyin;
    NSMutableArray *array = [manger arrayFromLib: pin];
    manger.winArr = array;
    //
        NSLog(@"array %@ %@*************",pin, array);
    
    // csy
//    NSMutableArray * array=[[NSMutableArray alloc] initWithObjects:@"ab",@"ab",@"cd",@"dc", nil];
    NSString *comp = @"";
    for (int i = 0; i< [array count]; i++) {
        NSString * wordStr=[array objectAtIndex:i];
        wordStr = [NSString stringWithFormat:@"%d.%@ ", i+1, wordStr];
        comp = [comp stringByAppendingString:wordStr];
    }
    NSString* compString = [[NSString alloc]initWithString:comp];

    NSLog(@"%@***", compString);
    
//    [imEngine appendComposeString:@""];
    [imEngine cleanComposeString];
    [[self candidatesWindow]update:[self client]];  // 更新候选窗
    
     [imEngine appendComposeString:compString];

  // 向光标处插入内嵌文字
//  [sender setMarkedText:compString
//         selectionRange:NSMakeRange(0, [compString length])
//       replacementRange:NSMakeRange(NSNotFound, NSNotFound)];
    
    // 向光标处插入内嵌文字
    NSString *insertString = pin;
    [sender setMarkedText:insertString
           selectionRange:NSMakeRange(0, [insertString length])
         replacementRange:NSMakeRange(NSNotFound, NSNotFound)];
    
    
//    NSMutableArray * res=[[NSMutableArray alloc] initWithObjects:@"00",@"181",@"292",@"33", nil];
//    NSLog(@"%@*************", res);
    
  [[self candidatesWindow]update:[self client]]; // 更新候选窗
}

-(void) commitComposedString:(id)sender index:(int) n
{
  SGDXIMEngine* imEngine = [SGDXIMEngine sharedObject];
  // 向光标处插入上屏文字
    
    manger.pinyin = @"";
    NSMutableArray *array = manger.winArr;
    // 更新文字 todo
//    NSString * wordStr=[array objectAtIndex:0];
    NSString * wordStr;
    if (n <= 10) {
        wordStr=[array objectAtIndex:n];
    } else {
        wordStr=[array objectAtIndex:0];
    }
    
    NSLog(@"n %d", n);
    [sender insertText:wordStr replacementRange:NSMakeRange(NSNotFound, NSNotFound)];

//  [sender insertText:[[SGDXIMEngine sharedObject] composeString]
//    replacementRange:NSMakeRange(NSNotFound, NSNotFound)];
    
  [imEngine cleanComposeString];
  [[self candidatesWindow]update:[self client]];  // 更新候选窗
}


- (BOOL)handleEvent:(NSEvent *)event client:(id)sender
{
//  NSLog(@"%@", event);
  if([event type] == NSKeyDown){
    unichar key = [[event characters] characterAtIndex:0];
    // 如果是字符则追加到写作串，并更新候选窗
       NSLog(@"%d", key);
      if (key == 8) {
          // delete
          NSUInteger len = manger.pinyin.length;
          if (len > 0) {
              manger.pinyin = [manger.pinyin substringToIndex:len-1];//截取下标7之前的字符串
          } else {
              manger.pinyin = @"";
          }
          NSLog(@"%@", manger.pinyin);
          // 删除一个字符 todo
          [sender setMarkedText:manger.pinyin
                 selectionRange:NSMakeRange(0, [manger.pinyin length])
               replacementRange:NSMakeRange(NSNotFound, NSNotFound)];
          
          return YES;
      }
      // (key >= '0' && key <= '9')
    if((key >= 'a' && key <= 'z')){
        
      [self appendComposedString:[event characters] client:sender];
      return YES;
    }
    // 如果是空格或回车且有写作串则上屏，并更新候选窗
    if(([event keyCode] == kVK_Space || [event keyCode] == kVK_Return)&&
      [[[SGDXIMEngine sharedObject] composeString] length] > 0)
    {
        [self commitComposedString:sender index:0];
      return YES;
    }
      
      if (key >= '0' && key <= '9') {
          int n = key - 49;
          [self commitComposedString:sender index:n];
          return YES;
      }
  }
  return NO;
}

- (NSUInteger)recognizedEvents:(id)sender {
  return NSEventMaskFlagsChanged | NSEventMaskKeyDown | NSEventMaskKeyUp;
}

@end
