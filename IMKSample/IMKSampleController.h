//
//  IMKSampleController.h
//  IMKSample
//
//  Created by palance on 17/3/22.
//  Copyright © 2017年 palanceli. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import <InputMethodKit/InputMethodKit.h>

@interface IMKSampleController : IMKInputController

@end



//声明类WordsLibManger
@interface WordsLibManger: NSObject
@property NSMutableArray *wordslib;
@property NSString *pinyin;
@property NSMutableArray *winArr;  // 候选窗
-(void) getWordsLib;
@end


//实现在类中声明的函数
@implementation WordsLibManger
-(void)getWordsLib {
    
    self.pinyin = @"";
    self.winArr = [NSMutableArray array];
    if ([self.wordslib count] > 0) {
        
        return;
    }
    NSLog(@"文件操作");
    // 文件操作
    NSString *path = @"/Users/Shared/github/inputjs/tesmain/teatmanin/teatmanin/new_pinyin_dict.txt";
    NSString *str = [NSString stringWithContentsOfFile:path encoding:NSUTF8StringEncoding error:nil];
    //        NSLog(@"%@",str);
    NSArray *array = [str componentsSeparatedByString:@"\n"];
    
    
    // 变量赋值
    NSMutableArray * words = [NSMutableArray array];
    for (int i = 0; i< [array count]; i++) {
        NSString * wordStr=[array objectAtIndex:i];
        NSArray * wordArr = [wordStr componentsSeparatedByString:@" "];;
        NSString * value = [wordArr objectAtIndex:0];
        NSString * key = [wordArr objectAtIndex:2];
        
        NSMutableDictionary * dict = [NSMutableDictionary dictionary];
        [dict setObject:value forKey:key];
        
        [words addObject:dict];
    }
    self.wordslib =  words;
};
-(NSMutableArray *)arrayFromLib: (NSString *)pin{
    NSMutableArray *words = self.wordslib;
    NSMutableArray * array = [NSMutableArray array];
    for (int i = 0; i< [words count]; i++) {
        NSDictionary * dict=[words objectAtIndex:i];
        for (NSString *s in [dict allKeys]) {
            if ([s isEqualToString:pin]) {
                // \U4e00\U4e00";
                NSString *value = [dict objectForKey:s];
                //                     NSLog(@"%@*************",value);
                [array addObject:value];
                if ([array count] == 10) {
                    return array;
                }
            }
        }
    }
    return array;
}
@end
